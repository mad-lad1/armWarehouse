cmake_minimum_required(VERSION 2.8.3)
project(placebot_description)
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros_control
  hardware_interface
  joint_state_publisher
  robot_state_publisher
  rviz
  transmission_interface
  xacro
  ira_laser_tools
)
catkin_package()

install(DIRECTORY launch urdf DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
