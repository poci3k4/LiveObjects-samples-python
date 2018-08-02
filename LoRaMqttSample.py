"""
Copyright (C) 2016 Orange

This software is distributed under the terms and conditions of the 'BSD 3'
license which can be found in the file 'LICENSE.txt' in this package distribution 
"""

from LoMqttConf import *
import LoMqttClient
import json

# On Windows, uncomment the 2 following lines to force prints (only works with Python3), or launch the script with "python -u LoRaMqttSample.py"
# import functools
# print = functools.partial(print, flush=True)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT Connected")
		
        # Subscription for all devices (pub sub) (deprecated and will be decommissioned in december 2018)
        # print client.subscribe("router/~event/v1/data/new/urn/lora/#")
        
        # Subscription for one specific device (pub sub) (deprecated and will be decommissioned in december 2018)
        # print client.subscribe("router/~event/v1/data/new/urn/lora/0123456789ABCDEF/#")

        # Subscription for all devices (pub sub) (new)
        # print(client.subscribe("router/~event/v1/data/new/typ/+/dev/+/con/lora/evt/+/grp/#"))
        
        # Subscription for one specific device (pub sub) (new)
        # print(client.subscribe("router/~event/v1/data/new/typ/+/dev/urn:lo:nsid:lora:0123456789ABCDEF/con/lora/evt/+/grp/#"))

        # Subscription for a fifo
        print(client.subscribe("fifo/myfifo"))
    else:
        print("Connected with result code "+str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    loPayload = json.loads(msg.payload.decode())
    print("timestamp "+loPayload["timestamp"]+", device "+loPayload["metadata"]["source"]+", payload "+loPayload["value"]["payload"])

print("Configuration:")
print("LO_MQTT_IP", LO_MQTT_IP)
print("LO_MQTT_PORT", LO_MQTT_PORT)
print("LO_USER_APIK", LO_USER_APIK)
	
# Create a Live Objects MQTT Client
client = LoMqttClient.LoMqttClient(LO_MQTT_IP, LO_MQTT_PORT, LO_USER_APIK)

# Set callbacks
client.on_connect = on_connect
client.on_message = on_message

client.connect()

client.loop_forever()
