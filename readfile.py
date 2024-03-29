import cv2
import face_recognition
import pandas as pd
from datetime import datetime

# Load known face encodings and names
# Assume known_face_encodings is a list of encoded face vectors and known_face_names is a list of corresponding names
# These should be loaded from the trained model
known_face_encodings = []
known_face_names = []

# Load CSV file if it exists
try:
    df = pd.read_csv('attendance.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Name', 'Time'])

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of that person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Record attendance
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        df = df.append({'Name': name, 'Time': dt_string}, ignore_index=True)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save attendance data to CSV file
df.to_csv('attendance.csv', index=False)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()