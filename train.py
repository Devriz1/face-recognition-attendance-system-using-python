import cv2
import numpy as np 
import os

PATH="data/"

recognizer=cv2.face.LBPHFaceRecognizer_create()


def getData():
	data=[]
	labels=[]
	dirs=os.listdir(PATH)
	c=0
	for item in dirs:
		for file in os.listdir(PATH+item+"/"):
			img=cv2.imread(PATH+item+"/"+file,0)
			data.append(img)
			labels.append(c)
		c+=1
	return data,np.array(labels)

print("Loading data...")
faces,labels=getData()




print("training...")
if os.path.exists('trained.yml'):
	recognizer.update(faces,labels)
else:
	recognizer.train(faces,labels)
print("Model trained..")
recognizer.save('trained.yml')
print("Saved to trained.yml")

