import requests
import time
import json
import yaml
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# protocol = "https"
# cluster_ip = "10.79.46.92"
# username = "admin"
# password = "Admin123"

# protocol = "https"
# cluster_ip = "172.20.55.33"
# username = "admin"
# password = "Maglev123"

protocol = "https"
cluster_ip = "172.20.98.188"
username = "admin"
password = "Auto_test123"

number_of_sites = 5
number_of_buildings = 10
number_of_floors = 10  # 200 floor in total

site_prefix = "Auto_Site_"
build_prefix = "Auto_Build_"
floor_prefix = "Auto_Floor_"

area_dic = {}
building_dic = {}
floor_dic = {}

get_token_url = '{}://{}/api/system/v1/auth/token'.format(protocol, cluster_ip)
get_domain_id_url = '{}://{}/api/ndp/v1/data/graph?query=sites()'.format(protocol, cluster_ip)


def get_auth_token():
    resp = requests.post(get_token_url, auth=(username, password), verify=False, timeout=30)
    if resp.status_code != 200:
        print('Failed to get authentication token. Code: {}, Error: {}'.format(resp.status_code, resp.text))
        return None

    resp_data = json.loads(resp.text)

    if 'Token' in resp_data:
        authToken = resp_data['Token']
        print(authToken)
        return authToken
    else:
        return None


auth_token = get_auth_token()

headers = {
    'X-AUTH-TOKEN': "{}".format(auth_token),
    'Content-type': "application/json",
    'USERNAME': username,
    'PASSWORD': password
}


def get_site_id(**payload):
    _get_site_id_url = f'{protocol}://{cluster_ip}/api/v1/group'

    data = requests.get(_get_site_id_url, params=payload, headers=headers, verify=False).json()
    return data


def get_all_domain_id():
    print(f"========== get floor id now ...... ==========")
    domain_id_response = requests.get(get_domain_id_url, headers=headers, verify=False)

    for item in domain_id_response.json():
        if item["properties"]["siteType"][0]["value"] == "floor":
            floor_dic[item["properties"]["name"][0]["value"]] = item["id"]
        elif item["properties"]["siteType"][0]["value"] == "building":
            building_dic[item["properties"]["name"][0]["value"]] = item["id"]
        elif item["properties"]["siteType"][0]["value"] == "area":
            area_dic[item["properties"]["name"][0]["value"]] = item["id"]
        else:
            print("!!!!!error!!!!!")

    print(f"========== Total area in database: {len(area_dic)} ==========")
    print(f"========== Total building in database: {len(building_dic)} ==========")
    print(f"========== Total floor in database: {len(floor_dic)} ==========")


def post_site(**payload):
    _get_site_id_url = f'{protocol}://{cluster_ip}/api/v1/group'
    global auth_token
    try:
        data = requests.post(_get_site_id_url, data=json.dumps(payload), headers=headers, verify=False).json()
        return data
    except requests.exceptions.ConnectionError:
        print("======================================================================")
        global auth_token
        auth_token = get_auth_token()
        print("======================================================================")


def create_sites():
    try:
        payload = {"groupName": "global"}
        data = get_site_id(**payload)
        time.sleep(1)
        _global_id = data["response"][0]["id"]

        for site in range(1, number_of_sites + 1):
            site_name = f"{site_prefix}{site}"
            site_id = area_dic.get(site_name, False)

            if not site_id:
                payload = {"groupTypeList": ["SITE"],
                           "parentId": "{}".format(_global_id),
                           "childIds": [""],
                           "name": "{}".format(site_name),
                           "id": "",
                           "additionalInfo": [{"nameSpace": "Location", "attributes": {"type": "area"}}]
                           }
                response = post_site(**payload)
                print(f"create site: {site_name}")
                # print(response)
                time.sleep(1)
                payload = {"groupName": site_name}
                data = get_site_id(**payload)
                time.sleep(1)
                site_id = data["response"][0]["id"]
            else:
                print(f'********* site {site_name} exists ************')

            for building in range((site - 1) * number_of_buildings + 1, site * number_of_buildings + 1):
                building_name = f"{build_prefix}{building}"
                building_id = building_dic.get(building_name, False)

                if not building_id:
                    payload = {"groupTypeList": ["SITE"],
                               "parentId": "{}".format(site_id),
                               "childIds": [""], "name": "{}".format(building_name),
                               "id": "",
                               "additionalInfo": [{"nameSpace": "Location",
                                                   "attributes": {"latitude": "37.407989",
                                                                  "longitude": "-121.952637",
                                                                  "address": "150 Tasman Drive, San Jose, California 95134, United States",
                                                                  "type": "building",
                                                                  "country": "United States"}}
                                                  ]}
                    response = post_site(**payload)
                    print(f"{site_name} > {building_name}")
                    # print(response)
                    time.sleep(1)

                    payload = {"groupName": building_name}
                    data = get_site_id(**payload)
                    time.sleep(1)
                    building_id = data["response"][0]["id"]

                else:
                    print(f'********* building {building_name} exists ************')

                for floor in range((building - 1) * number_of_floors + 1, building * number_of_floors + 1):
                    floor_name = f"{floor_prefix}{floor}"
                    floor_id = floor_dic.get(floor_name, False)

                    if not floor_id:
                        payload = {"groupTypeList": ["SITE"],
                                   "parentId": "{}".format(building_id),
                                   "childIds": [""],
                                   "name": "{}".format(floor_name),
                                   "id": "",
                                   "additionalInfo": [
                                       {"nameSpace": "Location", "attributes": {"type": "floor"}}]}
                        response = post_site(**payload)
                        print(f"{site_name} > {building_name} > {floor_name}")
                        # print(response)
                        time.sleep(1)
                    else:
                        print(f'********* floor {floor_name} exists ************')

        print('********* site creation successful ************')
    except KeyError:
        print('************** site creation failed : Config Error ****************')
        print(KeyError)


if __name__ == '__main__':
    get_all_domain_id()
    create_sites()
