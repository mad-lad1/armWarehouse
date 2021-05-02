#!/usr/bin/env python

import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

def main():
    box_state = ModelState()
    box_state.model_name = "red_box"            
    box_state.pose.position.x = 4.587541
    box_state.pose.position.y = -4.298763       #new pose of red_box
    box_state.pose.position.z = 0.0

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState) #apply the change in pose by calling the service
        resp = set_state(box_state)

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

