#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import subprocess
import rospy
import rosparam
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32MultiArray
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle

class MycobotHwInterface:
    def __init__(self):
        port_str = rospy.get_param("/hardware_interface/mycobot_port", "default")
        if port_str == "default":
            port = subprocess.check_output(['echo -n /dev/ttyUSB*'], shell=True)
        else:
            port = subprocess.check_output(['echo -n ' + port_str], shell=True)

        self.mycobot_ = MyCobot(port)
        self.mycobot_.power_on()

        rospy.init_node('mycobot_hw_interface', anonymous=True)
        #self.joint_state_msg_pub_ = rospy.Publisher('joint_states_array', Float32MultiArray, queue_size=10)
        self.joint_state_msg_pub_ = rospy.Publisher('joint_states', JointState, queue_size=10)
        self.joint_cmd_sub = rospy.Subscriber("joint_cmd_array", Float32MultiArray, self.jointCommandCallback)

        self.rate_ = rospy.Rate(10) # 10hz

        self.joint_state_array_ = []
        JOINT_NUMBER = 6
        for tmp in range(JOINT_NUMBER):  # initialize array
            tmp = 0.0
            self.joint_state_array_.append(tmp)
        self.pre_data_list = []
        self.first_flag = True

    def main_loop(self):
        while not rospy.is_shutdown():
            self.joint_state_msg_sender()
            self.rate_.sleep()
    
    def joint_state_msg_sender(self):
        angles = self.mycobot_.get_radians()
        for index, value in enumerate(angles):
            if index != 2:
                value *= -1
            self.joint_state_array_[index] = value

        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = ["arm1_joint", "arm2_joint", "arm3_joint", "arm4_joint", "arm5_joint", "arm6_joint"]
        joint_state_msg.position = self.joint_state_array_
        joint_state_msg.velocity = [0.0] * 6
        joint_state_msg.effort = [0.0] * 6

        self.joint_state_msg_pub_.publish(joint_state_msg)

    def jointCommandCallback(self, msg):
        data_list = []
        for index, value in enumerate(msg.data):
            if index != 2:
                value *= -1
            data_list.append(value)

        if self.first_flag:
            for value in data_list:
                self.pre_data_list.append(value)
            self.first_flag = False

        if self.pre_data_list != data_list:
            rospy.loginfo(rospy.get_caller_id() + "%s", msg.data)  # 修正箇所
            self.mycobot_.send_radians(data_list, 80)
            self.pre_data_list = []
            for value in data_list:
                self.pre_data_list.append(value)

if __name__ == '__main__':
    try:
        mc_hw_if = MycobotHwInterface()
        mc_hw_if.main_loop()
    except rospy.ROSInterruptException:
        pass

