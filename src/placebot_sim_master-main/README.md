# placebot_sim

ROS packages used to simulate placebot in a gazebo environment.

Placebot is robot base that featuring:
- 4 omni-directional wheels each capable of free 360 degrees steering angle.
- 2 sick-s300 lidar sensors mounted on opposite corners allowing a 360 degrees coverage and 30 meters range scans.

Packages contain the robot model description including sensors and actuators, base controller, gazebo plugins and supplementary scripts.

Published topics:
- /odom (nav_msgs/Odometry
- /scan (sensor_msgs/LaserScan)

Subscribed topics:
- /cmd_vel (geometry_msgs/Twist)

Implemented packages:
- g-mapping for SLAM
- AMCL for localization
- Navigation stack for autonomous navigation
