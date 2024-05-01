#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
import random

def callback(data):
    if data.range < 3:  
        turn() 
    else:
        move_forward()  

def move_forward():
    vel_msg = Twist()
    vel_msg.linear.x = -0.5
    vel_msg.angular.z = 0.0
    pub.publish(vel_msg)

def turn():
    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = random.randint(0, 5)
    pub.publish(vel_msg)

rospy.init_node('robot_controller')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/ultrasonic', Range, callback)
rospy.spin()
