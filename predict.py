import numpy as np
import cv2
import os
import csv 
from datetime import datetime

cap=cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('face.xml')
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("trained.yml")
# Open a CSV file in write mode to store attendance data
csv_file = open('attendance.csv', 'a', newline='')
csv_writer = csv.writer(csv_file)
# Write header row if file is empty
if os.path.getsize('attendance.csv') == 0:
    csv_writer.writerow(['Name', 'Time'])

def loadLabels():
	labels=[]
	for i in os.listdir("data/"):
		labels.append(i)
	return labels

labels=loadLabels()

while(True):
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    

    faces = face_cas.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        ids,_=rec.predict(gray[y:y+h,x:x+w])
        name=labels[ids]



         # Write attendance data to CSV (name and current time)
        csv_writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

        cv2.putText(frame,name,(y,x),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
 
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
              break

cap.release()
cv2.destroyAllWindows()
