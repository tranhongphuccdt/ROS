#! /usr/bin/env python
import rospy
from std_msgs.msg import Int64

if __name__=='__main__':
    rospy.init_node('number_publisher')
    pub = rospy.Publisher("/number",Int64, queue_size = 10)
    counter = 0
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        Value = Int64()
        Value.data = counter;
        pub.publish(Value)
        counter +=1
        rate.sleep()
    rospy.LOG("Node was stopped")

