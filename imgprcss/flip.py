import cv2
# grab the dimensions of the image and calculate the center
# of the image
image = cv2.imread("c:/python27/code/imgprcss/data/jura.jpg")
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# rotate the image by 180 degrees, and scale which is 1
M = cv2.getRotationMatrix2D(center, 180, 1.0) #variable for rotating matrix
rotated = cv2.warpAffine(image, M, (w, h)) #image, matrix, output dimension
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
