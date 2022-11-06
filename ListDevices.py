import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
devices_url = "https://<dirigera ip>:8443/v1/devices"
headers = { "Authorization": "Bearer <replace this text with access_token from GetAccessToken.py>"}

response = requests.get(devices_url, headers=headers, verify=False);
print(json.dumps(response.json(), indent=2))

# Check for a device id in the response and use it in ControlLamp.py to turn that lamp on or off