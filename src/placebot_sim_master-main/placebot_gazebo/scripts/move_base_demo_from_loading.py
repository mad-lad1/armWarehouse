#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from map_server.srv import LoadMap

reached = False

def change_map(zone_name):
    rospy.wait_for_service('change_map')
    try:
        #set up service for changing map
        switch_map = rospy.ServiceProxy('change_map', LoadMap)
        
        #switch map based on zone
        if zone_name != "LoadingZone":
            #Zone X reached. Changing map to go to the loading zone
            changing_maps = switch_map(map_path='/home/user/catkin_ws/src/placebot_sim_master-main/placebot_gazebo/maps/TO.yaml')
        else:
            #Loading Zone reached. Changing map to go to Zone X
            changing_maps = switch_map(map_path='/home/user/catkin_ws/src/placebot_sim_master-main/placebot_gazebo/maps/FROM.yaml')

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def movebase_client(zone_name, point_of_interest, reached):

    ns = rospy.get_namespace().strip('/')

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = ns + "/world"

    if zone_name == "ZoneA":
        if point_of_interest == "zoneTolane": #moving from loading zone to 1st point of interest
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        elif point_of_interest == "laneTozone": #moving from point of interest to zone
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0

    elif zone_name == "ZoneB":
        if point_of_interest == "zoneTolane":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        elif point_of_interest == "laneTozone":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
    elif zone_name == "ZoneC":
        if point_of_interest == "zoneTolane":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        elif point_of_interest == "laneTozone":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
    elif zone_name == "ZoneD":
        if point_of_interest == "zoneTolane":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        elif point_of_interest == "laneTozone":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
    elif zone_name == "LoadingZone":
        if point_of_interest == "zoneTolane":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        elif point_of_interest == "laneTozone":
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 4.004342
            goal.target_pose.pose.position.y = 10.018601
            goal.target_pose.pose.orientation.w = 1.0
        

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        if point_of_interest == "laneTozone": #only if navigating from lane to zone and reached desitnation
            change_map(zone_name) #change map
            reached = True #reached goal destination
        return client.get_result() #this also returns whether the goal was reached or not however for both points of interest and zones


if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client('ZoneA', 'zoneTolane', reached) #navigate from zoneTolane
        # or reached = movebase_client('ZoneA') with no need for the extra parameter in the function
        if result:
            rospy.loginfo("Goal execution from zone to lane done!")
        
        result = movebase_client('ZoneA', 'laneTozone', reached) #navigate from laneTozone
        
        if result:
            rospy.loginfo("Goal destination reached")

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")