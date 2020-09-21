#! /usr/bin/env python

import rospy

from std_srvs.srv import Empty, EmptyRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_move_in_circle_service_client')

rospy.wait_for_service('/move_bb8_in_circle')

bb8_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

bb8_object = EmptyRequest()

result = bb8_service()
print result
