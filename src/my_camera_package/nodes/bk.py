# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

# 顔検知器の作成 (OpenCVのHaar-cascadeを使用)
face_cascade = cv2.CascadeClassifier("/home/elephant/catkin_ws/src/my_camera_package/haarcascade_frontalface_default.xml")

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

                # Convert to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # Draw rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Publish the image with faces highlighted
                image_pub.publish(ros_image)
            except Exception as e:
                rospy.logerr("Error: %s" % e)

        rate.sleep()

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

