## 接続

ssh -Y elephant@192.168.0.7

For ($i=1; $i -le 24; $i++) {
    $ip = "192.168.0." + $i
    Write-Host "Trying to connect to $ip"
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no -Y elephant@$ip
}

## 簡易テストby mycobot

/catkin_ws/work
python3 /home/elephant/catkin_ws/work/test.py
python3 /home/elephant/catkin_ws/work/test2.py

## 初期設定? 覚えてない

https://note.com/npaka/n/n600b473e34f4
docker images
docker rmi id
docker image prune -a
PI_PORT ="/dev/ttyTHS1"
#PI_PORT ="/dev/ttyTHS2"

## 手順

ros立ち上げ
roscore
rosnode list
rostopic list
roslaunch mycobot_moveit mycobot_moveit_control.launch



## ローカル初期設定 fro remote rviZ
apt install tigervnc-standalone-server tigervnc-xorg-extension
chmod +x ~/.vnc/xstartup
vi ~/.vnc/config
    -listen tcp
    -listen 0.0.0.0
vi ~/.vnc/xstartup
    #!/bin/sh
    unset SESSION_MANAGER
    unset DBUS_SESSION_BUS_ADDRESS
    startxfce4 &


## リモートコマンド for remote rviz
https://tigervnc.org/からダウンロード
vncサーバー立ち上げ
echo $DISPLAY
export DISPLAY=:1
vncserver -kill :1
vncserver -localhost no
netstat -tulpn | grep Xtigervnc
やっと接続可能。
192.168.0.14:5901

## カメラ調整
/camera/image_raw
ls -l /dev/video*
groups $USER
v4l2-ctl --list-formats-ext --device /dev/video0
gst-launch-1.0 v4l2src device=/dev/video0 ! 'image/jpeg,width=640,height=480,framerate=30/1' ! jpegdec ! videoconvert ! autovideosink
roslaunch mycobot_moveit mycobot_moveit_camera.launch





リンク
https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.1-280/2.1.7-JN-2023.html