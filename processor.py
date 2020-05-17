#processor.py
#sits in ubuntu cloud vsi and subscribes to cloud mqtt broker for topic 'faces_topic'
#then sticks in s3 storage
#mosquitto_sub -t faces_topic -h broker

import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
    print("message received!")
    msg = msg.payload
    file_name="mybucket/face_"+str(x)
    image_file=open(file_name,"w")
    n=image_file.write(msg)
    image_file.close()
    x+=1

x=0
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message


# go into a loop
local_mqttclient.loop_forever()