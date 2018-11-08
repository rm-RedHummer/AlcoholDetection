import cv2
import matplotlib.pyplot as plt
import time

def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
    #just making a copy of image passed, so that passed image is not changed
    img_copy = colored_img.copy()
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)
     #go over list of faces and draw them as rectangles on original colored img

    for (x,y,w,h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img_copy

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

image = cv2.imread('C:/python27/code/thesis/data/test9.jpg')
haar_face_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_frontalface_default.xml')

faces_detected_img = detect_faces(haar_face_cascade,image)

# plt.imshow(convertToRGB(faces_detected_img))
cv2.imshow('Test Imag', faces_detected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
