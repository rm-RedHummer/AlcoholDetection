import cv2
import numpy as np
img = cv2.imread('C:/python27/code/thesis/data/iris1.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
thimg = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,9,12)

indices = np.where(thimg == [0])
coor = zip(indices[0],indices[1])

#create white image
whiteimg = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
whiteimg[:] = (255,255,255)

cv2.circle(whiteimg,(coor[0][0],coor[0][1]),30,(0,0,255),1)
white_indices = np.where(whiteimg == [0,0,255])
white_coor = zip(white_indices[0],white_indices[1])
print white_coor

cv2.imshow('detected circles',whiteimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
