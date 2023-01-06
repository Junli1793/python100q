import json
import requests
import time
from collections import OrderedDict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# protocol = "https"
# cluster_ip = "10.195.64.95"
# username = "admin"
# password = "Maglev123"

protocol = "https"
cluster_ip = "10.74.14.53"
username = "admin"
password = "Admin123"

floor_prefix = "Auto_Floor_"
floor_no_start = 75
floor_no_end = 100
ap_per_floor = 100

get_token_url = '{}://{}/api/system/v1/auth/token'.format(protocol, cluster_ip)
graph_query_url = '{}://{}/api/ndp/v1/data/graph?query'.format(protocol, cluster_ip)
get_domain_id_url = '{}://{}/api/ndp/v1/data/graph?query=sites()'.format(protocol, cluster_ip)

get_unassigned_ap_graph_query = ["g.V().hasLabel('allDeviceHealthScoreAgg_1_min').has('deviceFamily','Unified AP')" +
                                 ".has('floorId', '').valueMap(true, 'uuid').toList()"]

assign_ap_payload = {"networkdevice": ["c4a41b8e-b166-48b6-ad65-178cd89113c2"]}

floor_id_list = []
ap_uuid_list = []


# get auth token
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


# get floor id
def get_domain_id(floor):
    # with open("floor_id.json", 'r') as jsonFile2:
    #     floor_id_list = json.load(jsonFile2)

    global floor_id_list

    for item in floor_id_list:
        floor_id = item.get(floor, False)
        if floor_id:
            print(f"========== {floor} => {floor_id} ==========")
            break

    return floor_id


def get_all_domain_id():
    # domain_id_file = './floor_id.json'
    print(f"========== get floor id now ...... ==========")
    domain_id_response = requests.get(get_domain_id_url, headers=headers, verify=False)

    global floor_id_list
    floor_id_list = [{item["properties"]["name"][0]["value"]: item["id"]} for item in domain_id_response.json() if
                     item["properties"]["siteType"][0]["value"] == "floor"]
    print(f"========== Total floor in database: {len(floor_id_list)} ==========")
    # with open(domain_id_file, 'w') as jsonFile2:
    #     json.dump(floor_id_list, jsonFile2)


def get_all_unassigned_aps():
    # unassigned_ap_file = './unassigned_ap.json'
    print(f"========== get unassigned AP now ...... ==========")
    unassgined_aps_response = requests.post(graph_query_url, data=json.dumps(get_unassigned_ap_graph_query),
                                            headers=headers, verify=False)
    global ap_uuid_list
    ap_uuid_list = [item["uuid"][0] for item in unassgined_aps_response.json()[0]]
    print(f"========== Total AP in database: {len(ap_uuid_list)} ==========")
    # with open(unassigned_ap_file, 'w') as jsonFile1:
    #     jsonFile1.write(json.dumps(unassgined_aps_response.json()))


def assign_aps_to_a_sepcific_floor(floor, ap_number):
    floor_id = get_domain_id(floor)

    if floor_id:
        assign_ap_url = '{}://{}/api/v1/group/{}/member'.format(protocol, cluster_ip, floor_id)

        # temp_list = jsonfile[0][-ap_number:]
        # del jsonfile[0][-ap_number:]
        global ap_uuid_list
        print(f"========== Total AP in database: {len(ap_uuid_list)} ==========")

        for n in range(0, ap_number):
            ap_uuid = ap_uuid_list.pop()
            assign_ap_payload["networkdevice"][0] = ap_uuid
            try:
                response = requests.post(assign_ap_url, data=json.dumps(assign_ap_payload), headers=headers,
                                         verify=False)
                if response.status_code != 202:
                    print(f"No.{str(n).zfill(3)}: assign AP {ap_uuid} to {floor} failed. ")
                else:
                    print(f"No.{str(n).zfill(3)}: assign AP {ap_uuid} to {floor} succeed. ")
                time.sleep(0.5)
            except requests.exceptions.ConnectionError:
                print("======================================================================")
                global auth_token
                auth_token = get_auth_token()
                print("======================================================================")
    else:
        print(f"========== {floor} does not exist!!!!! ==========")


if __name__ == '__main__':
    get_all_domain_id()
    get_all_unassigned_aps()

    # with open("unassigned_ap.json", 'r+') as jsonFile:
    #     unassigned_aps = json.load(jsonFile, object_pairs_hook=OrderedDict)

    for i in range(floor_no_start, floor_no_end):
        floor_name = f"{floor_prefix}{i}"
        assign_aps_to_a_sepcific_floor(floor_name, ap_per_floor)
