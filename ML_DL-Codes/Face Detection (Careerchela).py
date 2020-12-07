# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:52:00 2020

@author: KIIT
"""
import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

video_capture = cv2.VideoCapture(0)

##4.35seconds
count=0;
while count<=50:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if face_extractor(frame) is not None:
        count+=1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Detected Candidate", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.putText(frame, "Congratulations!", (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
    else:
        cv2.putText(frame, "No Detected Candidate", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)  
        

        

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

