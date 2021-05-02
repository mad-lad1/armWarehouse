#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
import tf
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

class map_navigation():

	def __init__(self): 
		# initiliaze
		rospy.init_node('map_navigation_demo', anonymous=False)
		
		# dictionary to store action client object for each robot
		self.aclientsDic = {}

	def addRobotClient(self, robotnb):
		# assign an integer id to the new robot
		nb = int(robotnb)
		movebaseserver = "/robot" + str(nb) + "/move_base"
		
		#check if it already exist
		if nb in self.aclientsDic:
			rospy.loginfo("this robot already exist, choose a new robot ID")
			return
		
		# define a move_base client to send goal requests to the move_base server
		ac = actionlib.SimpleActionClient(movebaseserver, MoveBaseAction)
		
		# wait for the action server to come up
		while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
			rospy.loginfo("Waiting for the move_base action server to come up")
		
		self.aclientsDic[nb] = ac

	def moveToGoal(self, robotnb, xGoal, yGoal, thetaGoal):
		# specify which robot to send commands to; robotnb [int]
		# specify the goal (x y z theta) values to send to the robot
		
		# check if robot client exist
		robotnb = int(robotnb)
		if robotnb not in self.aclientsDic:
			rospy.loginfo("this robot does not exist, choose an existing robot number")
			return
		ac = self.aclientsDic[robotnb]
		
		# declare new goal object
		goal = MoveBaseGoal()

		# set up the frame parameters
		goal.target_pose.header.frame_id = "/robot" + str(robotnb) + "/map"
		goal.target_pose.header.stamp = rospy.Time.now()

		# moving towards the goal*/
		odom_quat = tf.transformations.quaternion_from_euler(0, 0, thetaGoal)
	
		goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
		goal.target_pose.pose.orientation.x = odom_quat[0]
		goal.target_pose.pose.orientation.y = odom_quat[1]
		goal.target_pose.pose.orientation.z = odom_quat[2]
		goal.target_pose.pose.orientation.w = odom_quat[3]

		rospy.loginfo("Sending goal location ...")
		ac.send_goal(goal)

		ac.wait_for_result(rospy.Duration(30))

		if(ac.get_state() ==  GoalStatus.SUCCEEDED):
			rospy.loginfo("You have reached the destination")	
			return True

		else:
			rospy.loginfo("The robot failed to reach the destination")
			ac.cancel_goal()
			return False

	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Quit program")
		rospy.sleep()

if __name__ == '__main__':
    try:
    	rospy.loginfo("Launching move base demo node.")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
