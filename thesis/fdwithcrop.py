import cv2
import matplotlib.pyplot as plt
import time

def detect_faces(f_cascade,e_cascade, colored_img, scaleFactor = 1.1):
    img_copy = colored_img.copy()
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    eye_list = []
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_copy[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            eye_list.append(roi_color[ey:ey+eh,ex:ex+ew])
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)


    return eye_list

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

image = cv2.imread('C:/python27/code/thesis/data/test3.jpg')
haar_face_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_eye.xml')

eyes_detected = detect_faces(haar_face_cascade,eye_cascade, image)

for index in range(len(eyes_detected)):
    cv2.imwrite("c:/python27/code/thesis/data/positive/eye"+str(index)+".jpg",eyes_detected[index])

# plt.imshow(convertToRGB(faces_detected_img))
# cv2.imshow('Test Imag', eyes_detected[1])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
