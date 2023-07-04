import sys
import rospy
import moveit_commander
import time

def pick_and_place():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('pick_and_place', anonymous=True)
    
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("mycobot_arm", robot_description="robot_description", ns="", wait_for_servers=10.0)

    # Get the current joint values
    current_joints = group.get_current_joint_values()

    # Go to the pick position
    rospy.loginfo("Setting pick position...")
    pick_position = list(current_joints)
    pick_position[0] += 0.4
    pick_position[1] += 0.4  # Modify the position of the 'arm2_joint'
    pick_position[2] += 0.4
    group.set_joint_value_target(pick_position)
    rospy.loginfo("Planning to pick position...")
    plan = group.plan()
    rospy.loginfo("Executing plan to pick position...")
    group.execute(plan, wait=True)
    
    # Simulate picking (in real world you would control gripper here)
    rospy.loginfo("Simulating picking...")
    time.sleep(2)

    # Go to the place position
    rospy.loginfo("Setting place position...")
    place_position = list(current_joints)
    place_position[0] -= 0.4
    place_position[1] -= 0.4  # Modify the position of the 'arm2_joint'
    place_position[2] -= 0.4
    group.set_joint_value_target(place_position)
    rospy.loginfo("Planning to place position...")
    plan = group.plan()
    rospy.loginfo("Executing plan to place position...")
    group.execute(plan, wait=True)

    # Simulate placing (in real world you would control gripper here)
    rospy.loginfo("Simulating placing...")

if __name__ == '__main__':
    pick_and_place()
