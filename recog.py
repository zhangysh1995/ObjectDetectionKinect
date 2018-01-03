import cv2
import numpy as np
from color_split import color_split
from sift2 import sift_match

class recog(object):
    def __init__(self, img):
        self.ori = img
        self.target = cv2.imread('target.jpg')

    def process(self):
        # ori = cv2.imread('blue.jpg')
        cp = color_split(self.ori)

        box, crpImg = cp.process()
        # cv2.imshow("res", crpImg)
        # cv2.waitKey(0)

        sm = sift_match()
        res, rate = sm.match(self.target, crpImg)
        print(rate)
        cv2.imshow("result", res)
        cv2.waitKey(0)