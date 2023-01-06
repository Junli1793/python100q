import jwt
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token_data = dict()
authentication = ('admin', 'Maglev123')
hostname = "10.28.115.204"
get_auth_token = requests.post(
    "https://" + hostname + "/api/system/v1/auth/token", verify=False, json={}, auth=authentication
)
auth_token = get_auth_token.json()["Token"]
token_data["token"] = {"name": "X-AUTH-TOKEN", "value": auth_token}
options = {"require": ["exp", "iss", "sub"], "verify_signature": False}
decoded_data = jwt.decode(auth_token, key="", verify=False, options=options)
tenantid = decoded_data['tenantId']
print(tenantid)
