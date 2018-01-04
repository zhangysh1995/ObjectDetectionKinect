import cv2
import numpy as np
from color_split import color_split
from sift2 import sift_match


class recog(object):
    def __init__(self, img, target):
        self.ori = img
        self.target = cv2.imread(target)
        self.res = None
        self.rate = None
        self.box = None
        self.crpImg = None
        self.detected = False
        self.process

    @property
    def process(self):
        # ori = cv2.imread('blue.jpg')
        cp = color_split(self.ori)

        self.box, self.crpImg = cp.process()
        # cv2.imshow("res", crpImg)
        # cv2.waitKey(0)

        sm = sift_match()
        res, rate = sm.match(self.target, self.crpImg)
        if res is None or rate is None:
            self.detected = False
        else:
            self.detected = True

    def if_exist(self):
        return self.detected
