#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image messagess
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

import time
import atexit
import os
from goForward import GoForward
from recog import recog

# Instantiate CvBridge
bridge = CvBridge()

rgb = Image()
depth = Image()

class ImageHandler():
	def __init__(self):
		rospy.init_node('cv_handler')
		atexit.register(self.shutdown)
		self.rgbSub, self.depthSub = self.initImageTopics()
		self.dist = 0
		
	def main(self):
		moveControl = GoForward()
	
		while not rospy.is_shutdown():
			# if find object, add to distance
			#	self.dist += 0.4
			#		if depth <= 0.5: rospy.loginfo(rospy.get_caller_id() + "...Approached object at 0.5m far ways...")
			# else: moveControl.moveForward(0.08, 2)
			moveControl.moveForward(0.08, 2)
			#do whatever with image
			time.sleep(2) # fake demo
	
	# initialize topics related to image
	def initImageTopics(self):
		rospy.loginfo(rospy.get_caller_id() + " ...image tools are initializing...")
		rgbSub = self.initRGB()
		depthSub = self.initDepth()
		rospy.loginfo(rospy.get_caller_id() + " ...image tools were initialized...")
		return rgbSub, depthSub
	
	def initRGB(self):
		image_topic = "/camera/rgb/image_raw"
		return rospy.Subscriber(image_topic, Image, self.image_callback)
	
	def initDepth(self):
		depth_topic = "/camera/depth/image_raw"
		return rospy.Subscriber(depth_topic, Image, self.imageDepth_callback)
	
	def image_callback(self, msg):
		#rospy.loginfo(rospy.get_caller_id() + " Received an image!")
		try:
			rgb = msg
			#cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError as e:
			print(e)
		else:
			cv2.imwrite('camera_image.jpeg', cv2_img)

	def rgb_exists(self):
		try:
			cv2_img = bridge.imgmsg_to_cv2(rgb, "bgr8")
		except CvBridgeError as e:
			print(e)
		else:
			target = "target2.jpg"
			cv2.imwrite('rgb.jpeg', cv2_img)

			test = cv2.imread("rgb.jpg")
			rg = recog(test, target)
			print(rg.if_exist())

	def imageDepth_callback(self, data):
		depth = data
		#rospy.loginfo(" Received depth info!")
	
	def shutdown(self):
		self.rgbSub.unregister()
		self.depthSub.unregister()
		rospy.loginfo(" ...Stop TurtleBot...")
		rospy.loginfo(" ...image tools are exiting...")
		rospy.sleep(1)

if __name__ == '__main__':
	handler = ImageHandler()
	handler.main()
