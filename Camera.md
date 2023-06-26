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