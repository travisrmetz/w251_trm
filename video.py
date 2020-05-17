import numpy as np
import cv2
import paho.mqtt.client as mqtt

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(0)
#face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


MQTT_HOST="172.18.0.2"
MQTT_PORT=1883
MQTT_TOPIC="faces_topic"
mqttclient = mqtt.Client()
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    cv2.waitKey(0)

    # We don't use the color information, so might as well save space
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        print ('face!',x,y,w,h)
        x2=x+w
        y2=y+h
        face=gray[y:y2,x:x2]
        #cv2.imshow('frame2',face)
        #cv2.waitKey(0)
        rc,png = cv2.imencode('.png', face)
        msg = png.tobytes()
        #print (len(png))
        
        mqttclient.publish(MQTT_TOPIC, payload=msg, qos=0, retain=False)
  
  
  
 
  