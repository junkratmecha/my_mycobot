import rospy
import sys
import moveit_commander

rospy.init_node('mycobot_calibration')
moveit_commander.roscpp_initialize(sys.argv)

group = moveit_commander.MoveGroupCommander("mycobot_arm", robot_description="robot_description", ns="", wait_for_servers=10.0)

positions = [[0.1, 0.2, 0.3], [0.2, 0.1, 0.3], [0.3, 0.2, 0.1]]

for position in positions:
    group.set_position_target(position)
    plan = group.plan()
    group.execute(plan)

