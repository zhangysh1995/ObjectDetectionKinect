#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def testPublish():
	pub = rospy.Publisher("publisher", String,queue_size=5)
	rospy.init_node("sender")
	rate = rospy.Rate(30)

	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def testSubscribe():
	rospy.init_node("receiver")
	rospy.Subscriber("publisher", String, callback)
	
	rospy.spin()

if __name__ == "__main__":
	testPublish()
	#testSubscribe()
