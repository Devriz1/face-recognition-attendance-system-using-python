# python-opencv-face-recognition
A simple face recognition in python using opencv. I used LBPH Recognizer which is provided by the opencv module.
It can detect multiple faces and recognize them. 
You can fine tune the model and improve it more by taking the value of confidence into consideration.
it is working in anaconda 

# Requirements
1. Python 3 https://pypi.org/project/pip/
Below two are the modules you can install with Pip.
2. Opencv Contrib (https://pypi.org/project/opencv-contrib-python/)
3. Numpy (https://pypi.org/project/numpy/)
4. opencv(https://pypi.org/project/opencv-python/)

Note: Make sure to use the OpenCv-contrib version. This module has the additonal functions which is needed for our FaceRecognition. To know more about it, look into their documentation. 

# How to use
1. Start by running the 'save_images.py' to save about 10 images of your face in the data/ folder.
2. Then run 'train.py' to load the images and train the recognizer , it will generate 'trained.yml'.
3. Run 'predict.py' to test the application.





