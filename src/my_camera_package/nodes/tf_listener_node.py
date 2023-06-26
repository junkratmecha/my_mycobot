#!/usr/bin/env python

import rospy
import tf

def main():
    rospy.init_node('tf_listener_node')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/world', '/camera', rospy.Time(0))
            rospy.loginfo("Translation: %s Rotation: %s" % (str(trans), str(rot)))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()

if __name__ == '__main__':
    main()

