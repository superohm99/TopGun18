import paho.mqtt.client as mqtt
import time

def onConnect(client, userData, flags, returnCode):
    if returnCode == 0:
        print("connectd")
        client.subscribe("Test")
    else:
        print("could not connect, return code:", returnCode)
        client.fail_connect = True

def onMessage(client, userData, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

brokerHostname = "172.18.32.1"
port = 1883

client = mqtt.Client("Client2")

client.on_connect = onConnect
client.on_message = onMessage
client.failed_connect = False

client.connect(brokerHostname, port)
client.loop_start()

try:
    i = 0
    while i < 15 and client.failed_connect == False:
        time.sleep(1)
        i = i + 1
    if client.failed_connect == True:
        print('Connection failed, exiting...')

finally:
    client.disconnect()
    client.loop_stop()
