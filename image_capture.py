import numpy as np
import serial
import time
import sys
import cv2

# Setup Communication path for arduino (In place of 'COM5' put the port to which your arduino is connected)
#arduino = serial.Serial('COM12', 9600)
#time.sleep(2)
#print("Connected to arduino...")

# Importing the Haarcascade for face detection
face_cascade = cv2.CascadeClassifier("D:/python_programming/pythonPrograms/F743B93JLQV1868.xml")

# To capture the video stream from webcam.
cap = cv2.VideoCapture(1)
cap.set(3, 640) # set video width
cap.set(4, 480)
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

# Read the captured image, convert it to Gray image and find faces1
while True:
    ret, img = cap.read()
    cv2.line(img, (500, 250), (0, 250), (0, 255, 0), 1)
    cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)

    # Detect the face and make a rectangle around it.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        count+=1
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.imwrite("D:/python_programming/pythonPrograms/Face_data/" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
        # Calculate center of the rectangle
        xx = int(x + (w / 2))
        yy = int(y + (h / 2))
        center = (xx, yy)

        # Sending data to Arduino
        #print("Center of Rectangle is:", center)
        #data = "X{0:f}Y{1:f}".format(xx, yy).encode('utf-8')
        #arduino.write(data)
        #print("Output = '" + str(data) + "'")

    # Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif count>=100:
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
