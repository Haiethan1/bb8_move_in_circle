#! /usr/bin/env python

import rospy
import rospkg

# Import the service message used by the service /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
exec_by_file_service = rospy.ServiceProxy('execute_trajectory', ExecTraj)
rospack = rospkg.RosPack()
exec_by_file_object = ExecTrajRequest()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
exec_by_file_object.file = traj
# Create the connection to the service

#traj_by_name_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type TrajByNameRequest
#traj_by_name_object = TrajByNameRequest()
# Fill the variable traj_name of this object with the desired value
#traj_by_name_object.traj_name = "release_food"
# Send through the connection the name of the trajectory to be executed by the robot
result = exec_by_file_service(exec_by_file_object)
#traj_by_name_service(traj_by_name_object)
# Print the result given by the service called
print result