## カメラ必要パッケージ
 apt install tigervnc-standalone-server tigervnc-xorg-extension
 apt-get install ros-me-cv-bridge

 catkin_create_pkg mycobot_camera rospy usb_cam

## 覚えてないが、configをいじったのだろう。

 config/ launch nodes
~/catkin_ws/src/my_camera_package/config/
usb_cam.yaml
    image_width: 640
    image_height: 480
    pixel_format: mjpeg
    camera_name: usb_cam
    camera_info_url: ""
    framerate: 30
    io_method: mmap

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


# 接続




# webカメラ
ls /dev/video*
roscore
export DISPLAY=:1
xterm
(カメラ発信)
rosrun usb_cam usb_cam_node _camera_info_url:=file:///home/elephant/catkin_ws/src/calibration/usb_cam.yaml _video_device:="/dev/video0" _pixel_format:="yuyv"
(カメラ受け取り)
rosrun image_view image_view image:=/usb_cam/image_raw

# キャリブレーション
rosrun camera_calibration cameracalibrator.py --size 10x7 --square 0.034 image:=/usb_cam/image_raw camera:=/usb_cam

# hand eye
rosrun usb_cam usb_cam_node _camera_info_url:=file:///home/elephant/catkin_ws/src/calibration/usb_cam.yaml _video_device:="/dev/video1" _pixel_format:="yuyv"
echo  $ROS_DISTRO
git clone https://github.com/IFL-CAMP/easy_handeye.git
rosparam list
roslaunch my_handeye_calibration calibrate.launch


# rviz
export DISPLAY=:1
rviz
roslaunch my_handeye_calibration artrack.launch
rosrun my_handeye_calibration ar_tlanslate.py
rostopic echo /ar_pose_marker