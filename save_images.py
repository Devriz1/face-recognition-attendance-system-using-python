import numpy as np
import cv2
import os


cap=cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('face.xml')
count=0
LIM=10

name=input("Enter name of person:")

def getCount(name):
    if os.path.exists('data/'+name+"/")==False:
        os.mkdir('data/'+name+"/")
    return len(os.listdir('data/'+name+"/"))

start=getCount(name)

while(count<LIM):
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cas.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if count < LIM:
        	cv2.imwrite('data/'+name+"/"+str(start+count) +".jpg",gray[y:y+h,x:x+w])
        	count+=1
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Images saved to data/"+name+"/")
