import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
devicesUrl = "https://<dirigera ip>:8443/v1/devices"
headers = { "Authorization": "Bearer <replace this text with access_token from GetAccessToken.py>"}

deviceAttributes = [
{ 
     "attributes": {
            "isOn": True
         }
    }
]
deviceUrl = devicesUrl + "/<replace this with a device id from the response from ListDevices>"
response = requests.patch(deviceUrl, headers=headers, json=deviceAttributes, verify=False)