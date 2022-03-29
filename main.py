import numpy as np
import cv2
from firebase import firebase
import serial
import time
import json

firebase = firebase.FirebaseApplication('https://suraksha-164e1-default-rtdb.firebaseio.com/')
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
k = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        k = 1
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    if (k == 1):
        name = {'Name': 'divya', }
        email = {'Email': 'divya@gmail.com', }
        no = {'Contact No': '9318375168', }
        alternative = {'Alternative contact': '9811777077', }
        address = {'Address': 'mumbai', }
        live_location = {'Live Location': '28.456,73.894', }
        data = {'Recognized Status': 'Positive', }
        result = firebase.post('/User Details/Name/', name)
        welo = firebase.post('/User Details/Email/', email)
        weo = firebase.post('/User Details/Contact/', no)
        fell = firebase.post('/User Details/Alternative/', alternative)
        rell = firebase.post('/User Details/address/', address)
        shit = firebase.post('/User Details/Location/', live_location)
        reslt = firebase.post('/Image data/Status/', data)
        b = 'ATD+919318375168;' + '\r\n'
        ser.write(b.encode())
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    else:
        data = {'Recognized Status': 'Negative', }
        result = firebase.post('/Image data/Status/', data)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
