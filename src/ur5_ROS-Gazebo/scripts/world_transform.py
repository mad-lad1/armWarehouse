#!/usr/bin/env python  
import roslib
roslib.load_manifest('ur5_notebook')

import rospy
import tf



if __name__ == '__main__':
    rospy.init_node('broadcaster_fixed')
    ns = rospy.get_namespace().strip('/')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 0.0),
                             (0.0, 0.0, 0.0, 1.0),
                             rospy.Time.now(),
                              ns + "/world",
                             "world")
       # rate.sleep()
       