from flask import Flask, render_template,request, redirect, url_for
import numpy as np
import cv2
import serial
app = Flask(__name__)

arduino = serial.Serial('COM4', 9600)

print ('Arduino initialized')

@app.route('/', methods = ['POST','GET'])
def definePage():
    if request.method == 'POST':
        # ka pag na click ang  turn on button
        if request.form['submit'] == 'Turn On': 
            print ('TURN ON')
            # pailawin ang LED on arduino
            arduino.write(b'A')
        # kapag na click ang turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
            # turn off LED on arduino
            arduino.write(b'B')

    # mga variables sa template page (templates/index.html)
    # kapag  post request sa webpage 
    
    # basahin ang  analog value galing sa photoresistor
    #readval = float(100);

    # ang default  page para ma display ang  template ng mga variables
    return render_template('index.html')

while(True):
    video_capture = cv2.VideoCapture(0) #ETO GAGAWIN MONG ZERO, ONE YAN TALAGA. 
    video_capture.set(3, 160)
    video_capture.set(4, 120)
    # Capture the frames
    ret, frame = video_capture.read()
        # Crop the image
    crop_img = frame[60:120, 0:160]
        # Convert to grayscale
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
        # Color thresholding
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
        # Find the contours of the frame
    image,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
       #SA TAAS NETO, LALAGYAN MO NG "image," sa unahan
        # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
        if cx >= 120:
            print "Turn Right!"
            arduino.write(b'R')
        elif cx < 120 and cx > 50:
            print "On Track!"
            arduino.write(b'F')
        elif cx <= 50:
            print "Turn Left"
            arduino.write(b'L')
        else:
            print "I don't see the line"
            arduino.write(b'S')
       #Display the resulting frame
    cv2.imshow('frame',crop_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if __name__ == "__main__":
    # patakbuhin ang webpage
    # do 0.0.0.0 para maka log sa webpage
    # gamitin ang network kung saan naka konecta ang computer
    app.run(host='0.0.0.0')
