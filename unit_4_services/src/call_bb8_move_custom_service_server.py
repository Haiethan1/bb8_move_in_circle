#! /usr/bin/env python

import rospy

from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest# you import the service message python classes generated from Empty.srv.
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_move_in_circle_service_client_custom')

rospy.wait_for_service('/move_bb8_in_circle_custom')

bb8_service = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

bb8_object = MyCustomServiceMessageRequest()

result = bb8_service(10)
print result
