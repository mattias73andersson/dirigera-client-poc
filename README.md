# dirigera-client-poc
Simple client for interacting with the IKEA Dirigera hub (made as a proof-of-concept)

To make it work:

1. Identify the Dirigera gateway ip on the local network
2. Use the ip in the code (GetAccesToken.py, ListDevices.py and ControlLamp.py)
3. Run GetAccessToken.py and use the access_token when running the ListDevices.py (Don't remove Bearer-string)
4. Run ControlLamp.py (don't forget to insert access_token) and use a id from the response in ListDevices.py

...and remember, this is proof-of-concept to test the local interface of the IKEA Dirigera gateway. The intention of writing this
code was just to see if it vas possible to connect to the gateway. The smell of the code is pretty bad ;.)

Other endpoins of the Dirigera gateway can be found by decompiling the IKEA Smart Home App.




