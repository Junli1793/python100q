import requests
import time
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# protocol = "https"
# cluster_ip = "10.79.46.92"
# username = "admin"
# password = "Admin123"
protocol = "https"
cluster_ip = "172.20.110.234"
username = "admin"
password = "Auto_test123"

site_prefix = "Auto_Site_"
build_prefix = "Auto_Build_"
floor_prefix = "Auto_Floor_"

floor_id_list = []
building_id_list = []
area_id_list = []

get_token_url = '{}://{}/api/system/v1/auth/token'.format(protocol, cluster_ip)
get_domain_id_url = '{}://{}/api/ndp/v1/data/graph?query=sites()'.format(protocol, cluster_ip)
delete_site_url = '{}://{}/api/v1/dna-maps-service/domains/{}'


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


# get floor id list, building id list, area id list
def get_domain_id():
    domain_id_response = requests.get(get_domain_id_url, headers=headers, verify=False)
    domain_id_resp = domain_id_response.json()
    for item in domain_id_resp:
        if item["properties"]["siteType"][0]["value"] == "floor" and item["properties"]["name"][0]["value"].startswith(
                floor_prefix):
            floor_id_list.append(item["id"])
        elif item["properties"]["siteType"][0]["value"] == "building" and item["properties"]["name"][0][
            "value"].startswith(build_prefix):
            building_id_list.append(item["id"])
        elif item["properties"]["siteType"][0]["value"] == "area" and item["properties"]["name"][0]["value"].startswith(
                site_prefix):
            area_id_list.append(item["id"])


def delete_floor(floor_id_list):
    for floor_id in floor_id_list:
        try:
            resp = requests.delete(delete_site_url.format(protocol, cluster_ip, floor_id), headers=headers,
                                   verify=False)
            time.sleep(1)
            if resp.status_code == 202:
                print("delete floor successfully, floor id is {}".format(floor_id))
            else:
                print("Failed to delete floor, floor id is {}".format(floor_id))
        except requests.exceptions.ConnectionError:
            print("======================================================================")
            global auth_token
            auth_token = get_auth_token()
            print("======================================================================")


def delete_building(building_id_list):
    for building_id in building_id_list:
        resp = requests.delete(delete_site_url.format(protocol, cluster_ip, building_id), headers=headers, verify=False)
        time.sleep(1)
        if resp.status_code == 202:
            print("delete building successfully, building id is {}".format(building_id))
        else:
            print("Failed to delete building, building id is {}".format(building_id))


def delete_area(area_id_list):
    for area_id in area_id_list:
        resp = requests.delete(delete_site_url.format(protocol, cluster_ip, area_id), headers=headers, verify=False)
        time.sleep(1)
        if resp.status_code == 202:
            print("delete area successfully, area id is {}".format(area_id))
        else:
            print("Failed to delete area, area id is {}".format(area_id))


if __name__ == '__main__':
    get_domain_id()

    # delete floor first
    delete_floor(floor_id_list)

    # delete building
    delete_building(building_id_list)

    # delete area
    delete_area(area_id_list)
