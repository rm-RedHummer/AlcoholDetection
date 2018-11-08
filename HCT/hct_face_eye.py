import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
            roi_eyes_gray = gray[ey:ey+eh, ex:ex+ew]
            roi_eyes_color = img[ey:ey+eh, ex:ex+ew]
            eye_img = cv2.medianBlur(roi_eyes_gray,5)
            c_eye_img = cv2.cvtColor(eye_img,cv2.COLOR_GRAY2BGR)
            circles = cv2.HoughCircles(eye_img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=10,maxRadius=30)
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

# import cv2
# face_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('C:\Python27\code\AItrain\haarcascade_eye.xml')
# cap = cv2.VideoCapture(0)
# while 1:
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.2, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
#
#     cv2.imshow('img',img)
#
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()
