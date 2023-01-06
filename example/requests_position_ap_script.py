# this file is to get all the APs on a floor, then position these APs to the map
import json
import requests
import time
from collections import OrderedDict

# need to refresh floor_name according to the floor you want to position APs
protocol = "https"
cluster_ip = "10.79.59.25"
get_domain_id_url = '{}://{}/api/ndp/v1/data/graph?query=sites()'.format(protocol, cluster_ip)
floor_name = "Floor 4"

# X-AUIH-Token should be refreshed every time execute this file
# username and password should be updated accordingly
headers = {
    'X-AUTH-TOKEN': "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZjlhODExZWFkOThlYzUwMzNmOTQ2YTAiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVmOWE4MTFkYWQ5OGVjNTAzM2Y5NDY5ZiJdLCJ0ZW5hbnRJZCI6IjVmOWE4MTFjYWQ5OGVjNTAzM2Y5NDY5ZCIsImV4cCI6MTYwNDQ4ODUyOSwiaWF0IjoxNjA0NDg0OTI5LCJqdGkiOiJmYmM5M2QwOC0xMmRiLTRhNzYtYTA4My1hZmQ1ZjgyZmM2YTgiLCJ1c2VybmFtZSI6ImFkbWluIn0.hr8aYGqEV1OvRbfXpzKI6QzQuIdCzjitm4fQO_GjMbwGS89NbxGmnAYSD3RR1i4j_4WU6w6Gw11EH-VWLF5Jiv0sgDnBYNaeq8ZUcTiZsXEKTjmdTL6xMr2HaeiPkvf5Ubii0c70kqbaoaXfjx3p3FwzH9HSHDDxTso5atV99tS_7MdPn0S8psod-6CMMNSdBmN0p2ufDCCLAwdinnfSk5QkUX7dolcpzuRkDlWY3OpTCd6JlANM9rGDm18Qk32CSJhTutOz3vB56KRa7cuEb36gYK-8SgXKBsyaNtRS6_FZuwjogBD8J0fp5_Q9NcBF1volFja_dpYfuvcOeLKMaw",
    'Content-type': "application/json",
    'USERNAME': "admin",
    'PASSWORD': "Admin123"
}

# get floor id
def get_domain_id():
    domain_id_response =  requests.get(get_domain_id_url, headers = headers, verify = False)
    domain_id_resp = domain_id_response.json()
    for item in domain_id_resp:
        if item["properties"]["name"][0]["value"] == floor_name:
            domain_id = item["id"]
            break
    return domain_id

domain_id = get_domain_id()

get_aps_on_a_floor_url = '{}://{}/api/v1/dna-maps-service/domains/{}/aps?pageSize=250'.format(protocol, cluster_ip, domain_id)

position_ap_url = '{}://{}/api/v1/dna-maps-service/domains/{}/aps'.format(protocol, cluster_ip, domain_id)

#position ap payload
payload = [
    {"attributes":
         {
             "instanceUuid":"b502628d-7123-4a1e-9c3c-51416d07b84c"
         },
     "position":
         {
            "x":55.95690265438785,
            "y":36.548376905742145,
            "z":10
         }
     }
]

def get_all_the_aps_on_a_floor():

    ap_json_file = './ap.json'

    aps_response = requests.get(get_aps_on_a_floor_url, headers = headers, verify = False)

    with open(ap_json_file, 'w') as jsonFile:
        jsonFile.write(json.dumps(aps_response.json()))

def position_aps():
    with open("ap.json") as jsonFile:
        jsonfile = json.load(jsonFile, object_pairs_hook=OrderedDict)
        print(jsonfile["items"])
        i = 1
        for item in jsonfile["items"]:
                ap_name = item["attributes"]["name"]
                payload[0]["attributes"]["instanceUuid"] = item["attributes"]["instanceUuid"]
                payload[0]["position"]["x"] = 8 * int(i/20) + 1
                payload[0]["position"]["y"] = round((i/20 - int(i/20))*100) + 1
                print(ap_name, payload)
                i += 1
                response = requests.put(position_ap_url, data=json.dumps(payload), headers=headers, verify=False)
                if response.status_code != 202:
                    resp = response.json()
                    print("=================", resp["items"][0]["name"], resp["items"][0]["instanceUuid"])
                time.sleep(10)

#get all the APs on a floor first
get_all_the_aps_on_a_floor()

#postion APs
position_aps()
