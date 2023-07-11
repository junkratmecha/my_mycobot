#!/usr/bin/env python

import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from visualization_msgs.msg import Marker, MarkerArray

def callback(alvar_markers):
    marker_array = MarkerArray()
    for alvar_marker in alvar_markers.markers:
        marker = Marker()
        marker.header = alvar_marker.header
        marker.id = alvar_marker.id
        marker.pose = alvar_marker.pose.pose
        marker.type = Marker.CUBE
        marker_array.markers.append(marker)

    pub.publish(marker_array)

rospy.init_node('alvar_to_marker')
sub = rospy.Subscriber('/ar_pose_marker', AlvarMarkers, callback)
pub = rospy.Publisher('/visualization_marker_array', MarkerArray, queue_size=10)
rospy.spin()
