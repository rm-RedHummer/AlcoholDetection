import numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('c:/python27/code/imgprcss/data/noised.jpg')
dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

cv2.imwrite("c:/python27/code/imgprcss/data/denoised.jpg",dst)
