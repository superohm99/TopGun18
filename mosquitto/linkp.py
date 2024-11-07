import paho.mqtt.client as mqtt
import time

brokerHostname = "172.18.32.1"
port = 1883

def onConnect(client, userData, flags, returnCode):
    if returnCode == 0:
        print("connect")
    else:
        print("could not connect, return code:", returnCode)

client = mqtt.Client("Client1")

client.on_connect = onConnect

client.connect(brokerHostname, port)
client.loop_start()

topic = "Test"
msgCount = 0

try:
    while msgCount < 10:
        time.sleep(1)
        msgCount += 1
        result = client.publish(topic, msgCount)
        status = result[0]
        if status == 0:
            print("Message "+ str(msgCount) + " is published to topic " + topic)
        else:
            print("Failed to send message to topic " + topic)
            if not client.is_connected():
                print("Client not connected, exitting...")
                break
finally:
    client.disconnect()
    client.loop_stop()
