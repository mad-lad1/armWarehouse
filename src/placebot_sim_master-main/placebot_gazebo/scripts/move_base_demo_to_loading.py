#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from map_server.srv import LoadMap


def change_map():
    rospy.wait_for_service('change_map')
    try:
        switch_map = rospy.ServiceProxy('change_map', LoadMap)
        changing_maps = switch_map(map_path='/home/user/catkin_ws/src/placebot_sim_master-main/placebot_gazebo/maps/FROM.yaml')
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def movebase_client():

    ns = rospy.get_namespace().strip('/')

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = ns + "/world"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0
    goal.target_pose.pose.position.y = 1.5
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        change_map()
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")