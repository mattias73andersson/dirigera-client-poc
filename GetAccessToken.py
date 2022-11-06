import requests
import hashlib
import base64
import random
import socket
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

CODE_ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
CODE_LENGTH = 128
authUrl = "https://<dirigera ip>:8443/v1/oauth/authorize"
tokenUrl = "https://<dirigera ip>:8443/v1/oauth/token"

def getChar():
    return CODE_ALPHABET[random.randrange(0, len(CODE_ALPHABET))]

def getCodeVerifier():
    s = ""
    for a in range(0, CODE_LENGTH):
        s += getChar()
    return s

def createCodeChallenge(codeVerifier: str):
    sha256Hash = hashlib.sha256()
    sha256Hash.update(codeVerifier.encode())
    digest = sha256Hash.digest()
    sha256HashAsBase64 = base64.urlsafe_b64encode(digest).rstrip(b'=').decode('us-ascii')
    return sha256HashAsBase64

codeVerifier = getCodeVerifier()
params = {
    "audience": "homesmart.local",
    "response_type": "code",
    "code_challenge": createCodeChallenge(codeVerifier),
    "code_challenge_method": "S256"
}
response = requests.get(authUrl, params=params,verify=False);
code = response.json()['code']

input('Wait for button pressed (actionbutton on Dirigera)...') # Press button on device and press a key in cmd-prompt to "release" code below afterwards

data = str("code=" + code + "&name=" + socket.gethostname() + "&grant_type=" + "authorization_code" + "&code_verifier=" + codeVerifier)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(tokenUrl, headers=headers, data=data, verify=False)
print(response.json()['access_token'])