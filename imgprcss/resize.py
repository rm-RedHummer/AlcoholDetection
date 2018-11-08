# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("c:/python27/code/imgprcss/data/jura.jpg")
#600 x 300 hw
r = 100.0 / image.shape[1] # ratio of the width to be 100
dim = (100, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
