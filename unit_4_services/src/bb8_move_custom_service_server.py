#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse# you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
import time

def my_callback(request):
    print "Request Data==> duration="+str(request.duration)
    response = MyCustomServiceMessageResponse()
    circ = Twist()
    circ.linear.x = 1.0
    circ.angular.z = .7
    pub.publish(circ)
    
    if request.duration > 4.0:
        response.success = True
        time.sleep(request.duration)
    else:
        response.success = False

    circ.linear.x = 0
    circ.angular.z = 0
    pub.publish(circ)
    return response # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_server_custom') 
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin() # maintain the service open.