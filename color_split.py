import cv2
import numpy as np

class color_split(object):
	def __init__(self, img):
		# set blue thresh
		self.lower_blue = np.array([78, 43, 46])
		self.upper_blue = np.array([110, 255, 255])
		# ori = cv2.imread('blue.jpg')
		self.ori  = img;
		self.copy = img.copy();

	def process(self):
		# change to hsv model
		hsv = cv2.cvtColor(self.ori, cv2.COLOR_BGR2HSV)

		# get mask
		mask = cv2.inRange(hsv, self.lower_blue, self.upper_blue)
		# cv2.imshow('Mask', mask)

		# dilating
		kernel_d = np.ones((8, 8), np.uint8)
		dilated = cv2.dilate(mask, kernel_d)
		# cv2.imshow('Dilated', dilated)

		# eroding
		kernel_e = np.ones((10, 10), np.uint8)
		eroded = cv2.erode(dilated, kernel_e)
		# cv2.imshow('Eroded', eroded)

		# contours detection
		contours, hierarchy = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		# cv2.drawContours(eroded, contours, -1, (255, 255, 255), 1)
		# cv2.imshow('Contour', eroded)

		maxContour = contours[0]
		for contour in contours:
			# print "max area:%d\n",cv2.contourArea(maxContour)
			# print "current area:%d\n", cv2.contourArea(contour)
			if cv2.contourArea(contour) > cv2.contourArea(maxContour):
				maxContour = contour
				#print "exchange"

		#cv2.drawContours(eroded, maxContour, -1, (255, 255, 255), 3)
		rect = cv2.minAreaRect(maxContour)
		box = np.int0(cv2.cv.BoxPoints(rect))
		# cv2.drawContours(copy, [box], -1, (0, 255, 0), 3)
		# cv2.imshow("contour", copy)

		# crop rectangle from ori
		Xs = [i[0] for i in box]
		Ys = [i[1] for i in box]
		x1 = min(Xs)
		x2 = max(Xs)
		y1 = min(Ys)
		y2 = max(Ys)
		height = y2 - y1
		width = x2 - x1
		crpImg = self.ori[y1:y1+height, x1:x1+width]

		return box, crpImg
		# cv2.imshow('Result', cropImg)
		# cv2.waitKey(0)

# x, y = rect[0]
# #cv2.circle(eroded, (int(x), int(y)), 3, (0, 255, 0), 5)
# width, height = rect[1]
# angle = rect[2]
#
# print 'width=', width, 'height=', height, 'x=', x, 'y=', y, 'angle=', angle
#cv2.rectangle(copy, (int(x - width / 2), int(y + height / 2)), (int(x + width / 2), int(y - height / 2)), (0,255,255), 3)
# cv2.imshow("contour", copy)

# detect blue
#res = cv2.bitwise_and(ori, ori, mask=eroded)