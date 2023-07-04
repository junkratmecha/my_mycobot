from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time
PI_PORT ="/dev/ttyTHS1" #or "/dev/ttyTHS2"
mc = MyCobot(PI_PORT, PI_BAUD)
mc.set_color(0, 0, 255)

mc.set_gripper_state(1, 0)
time.sleep(3)
mc.set_gripper_state(0, 0) 
time.sleep(3)
mc.set_gripper_state(1, 0)

# https://note.com/npaka/n/nd3e8b541e35d