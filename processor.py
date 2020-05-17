#processor.py
#sits in ubuntu cloud vsi and subscribes to cloud mqtt broker for topic 'faces_topic'
#then sticks in s3 storage
#mosquitto_sub -t faces_topic -h broker

import paho.mqtt.client as mqtt
import os
import cv2

LOCAL_MQTT_HOST="broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
    print("message received!")
    #msg = msg.payload
    image_array = np.fromstring(msg.payload, np.uint8)
	image = cv2.imdecode(nparr,  cv2.IMREAD_GRAYSCALE)
    file_name=os.path.join(os.getcwd(),"mybucket/face.png"+str(int(time.time()))+".png")    
    cv2.imwrite(file_name, image)

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message


# go into a loop
local_mqttclient.loop_forever()
