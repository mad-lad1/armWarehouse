cmake_minimum_required(VERSION 2.8.3)
project(placebot_gazebo)
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  placebot_description
  controller_manager
  controller_manager_msgs
  effort_controllers
  gazebo_ros
  joint_state_controller
  rospy
  std_msgs
  tf
  tf2
  move_base
  gmapping
  map_server
  turtlebot_teleop
)

catkin_package()

install(DIRECTORY config launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
