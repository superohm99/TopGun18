from workspace import app, socketio
import threading
import paho.mqtt.client as mqtt
import time

# ฟังก์ชันที่ใช้จัดการเมื่อเชื่อมต่อกับ MQTT Broker
def onConnect(client, userData, flags, returnCode):
    if returnCode == 0:
        print("Connected successfully")
        mqtt_client.subscribe("Test")  # Subscribe to topic 'Test' เมื่อเชื่อมต่อสำเร็จ
    else:
        print(f"Could not connect, return code: {returnCode}")
        mqtt_client.failed_connect = True

# ฟังก์ชันที่ใช้จัดการเมื่อได้รับข้อความจาก MQTT Broker
def onMessage(client, userData, message):
    print(f"Received message: {str(message.payload.decode('utf-8'))}")

# กำหนด IP และ port ของ MQTT Broker
brokerHostname = "localhost"  # เปลี่ยนให้เป็น IP ของ MQTT Broker
port = 1883

# สร้าง MQTT client
mqtt_client = mqtt.Client("Clientohm")

# ตั้งค่า callback functions
mqtt_client.on_connect = onConnect
mqtt_client.on_message = onMessage
mqtt_client.failed_connect = False

# ฟังก์ชันเพื่อเชื่อมต่อ MQTT และเริ่ม loop
def start_mqtt():
    print("uck1")
    try:
        # เริ่ม loop ของ MQTT Client ใน background thread
        print("uck2")
        mqtt_client.connect(brokerHostname, port)  # แก้ไขตรงนี้
        mqtt_client.loop_start()  # เริ่ม loop ของ MQTT client
        # print(mqtt_client)
        # เชื่อมต่อกับ MQTT Broker
        
        # ใช้เวลารอให้การเชื่อมต่อสำเร็จและทำงานอยู่
        while not mqtt_client.is_connected():
            print("Waiting for MQTT connection...")
            time.sleep(1)  # รอการเชื่อมต่อ
        print("Connected to MQTT Broker!")
    except Exception as e:
        print(f"Error connecting to MQTT Broker: {e}")

# เริ่ม Thread ใหม่สำหรับการเชื่อมต่อ MQTT
if __name__ == "__main__":
    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.daemon = True 
    mqtt_thread.start()
    # เริ่ม Flask app และ SocketIO
    socketio.run(app, host="0.0.0.0", debug=True, port=5888, allow_unsafe_werkzeug=True)
