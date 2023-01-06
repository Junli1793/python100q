import json
import requests
import time
from collections import OrderedDict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

protocol = "https"
cluster_ip = "10.195.64.95"
username = "admin"
password = "Maglev123"

floor_prefix = "Floor1_Site_"
floor_no_start = 201
floor_no_end = 601
ap_per_floor = "all"

floor_id_list = []
ap_uuid_list = []

get_token_url = '{}://{}/api/system/v1/auth/token'.format(protocol, cluster_ip)
graph_query_url = '{}://{}/api/ndp/v1/data/graph?query'.format(protocol, cluster_ip)
get_domain_id_url = '{}://{}/api/ndp/v1/data/graph?query=sites()'.format(protocol, cluster_ip)


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

unassign_ap_url = '{}://{}/api/v1/group/{}/member/{}'
ap_graph_query = "g.V().hasLabel('allDeviceHealthScoreAgg_1_min').has('floorId', '{}').valueMap(true, 'uuid').toList()"


def get_all_assigned_aps(domain_id):
    graph_query_payload = [ap_graph_query.format(domain_id)]
    print(f"========== get assigned AP now ...... ==========")
    assgined_aps_response = requests.post(graph_query_url, data=json.dumps(graph_query_payload), headers=headers,
                                          verify=False)
    global ap_uuid_list
    ap_uuid_list = [item["uuid"][0] for item in assgined_aps_response.json()[0]]
    print(f"========== Total AP in floor: {len(ap_uuid_list)} ==========")


def unassign_aps_from_a_sepcific_floor(floor_name, ap_number):
    floor_id = get_domain_id(floor_name)
    if not floor_id:
        print(f'========== site {floor_name} does not exist!!! ==========')
        return
    get_all_assigned_aps(floor_id)

    global ap_uuid_list
    if ap_number == "all" or ap_number == "ALL":
        ap_number = len(ap_uuid_list)

        # while len(ap_uuid_list) > 0:
    for n in range(ap_number):
        ap_uuid = ap_uuid_list.pop()
        try:
            response = requests.delete(unassign_ap_url.format(protocol, cluster_ip, floor_id, ap_uuid), headers=headers,
                                       verify=False)
            if response.status_code != 202:
                print("Failed to unassign the ap, apUuid is {}".format(ap_uuid))
            else:
                print(f"unassign ap No.{n} successfully, apUuid is {ap_uuid}")
            time.sleep(2)
        except requests.exceptions.ConnectionError:
            print("======================================================================")
            global auth_token
            auth_token = get_auth_token()
            print("======================================================================")
    # get_all_assigned_aps(floor_id)


def get_all_domain_id():
    print(f"========== get floor id now ...... ==========")
    domain_id_response = requests.get(get_domain_id_url, headers=headers, verify=False)

    global floor_id_list
    floor_id_list = [{item["properties"]["name"][0]["value"]: item["id"]} for item in domain_id_response.json() if
                     item["properties"]["siteType"][0]["value"] == "floor"]
    print(f"========== Total floor in database: {len(floor_id_list)} ==========")


# get floor id
def get_domain_id(floor):
    global floor_id_list

    for item in floor_id_list:
        floor_id = item.get(floor, False)
        if floor_id:
            print(f"========== {floor} => {floor_id} ==========")
            break

    return floor_id


if __name__ == '__main__':
    get_all_domain_id()

    for i in range(floor_no_start, floor_no_end):
        floor_name = f"{floor_prefix}{i}"
        unassign_aps_from_a_sepcific_floor(floor_name, ap_per_floor)
