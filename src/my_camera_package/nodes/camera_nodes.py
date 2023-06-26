#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def main():
    rospy.init_node('camera_node')

    # Image publisher
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=1)

    # Initialize CvBridge
    bridge = CvBridge()

    # Set the camera device index or the video file name
    cam = cv2.VideoCapture(0)
    

    # Check if the camera is opened
    if not cam.isOpened():
        rospy.logerr("Failed to open the camera")
        return

    # Set the frame rate
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        # Capture a frame from the camera
        ret, frame = cam.read()

        if ret:
            try:
                # Convert the OpenCV image to a ROS message
                ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
                image_pub.publish(ros_image)
            except Exception as e:
                rospy.logerr("Error: %s" % e)

        rate.sleep()

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
