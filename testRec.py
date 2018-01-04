import cv2
import numpy as np
from recog import recog

target = cv2.imread("target.jpg")
test = cv2.imread("test_img.jpg")
#test = cv2.imread("blue.jpg")

rg = recog(test)
print(rg.if_exist())
