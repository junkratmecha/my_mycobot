import sys
import rospy
import moveit_commander

def set_start_position():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('set_start_position', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander("mycobot_arm", robot_description="robot_description", ns="", wait_for_servers=10.0)

    rospy.loginfo("MoveIt! and ROS Initialized")

    # Set planning time
    rospy.loginfo("Planning time set")

    # Set joint values for the start position
    joint_goal = [0, 0.5, 0, 0, 0, 0]
    rospy.loginfo("Setting start joint goals: {}".format(joint_goal))

    # Compute plan
    plan = group.plan(joint_goal)
    rospy.loginfo("Plan computed")

    # Execute plan
    group.execute(plan, wait=True)
    rospy.loginfo("Start position reached")

    # Shutdown MoveIt!
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    set_start_position()
