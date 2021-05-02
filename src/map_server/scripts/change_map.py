#!/usr/bin/env python

import rospy
from map_server.srv import LoadMap

def change_map():
    rospy.wait_for_service('change_map')
    try:
        switch_map = rospy.ServiceProxy('change_map', LoadMap)
        changing_maps = switch_map(map_path='/home/user/catkin_ws/src/placebot_sim_master-main/placebot_gazebo/maps/wh3.yaml')
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    change_map()