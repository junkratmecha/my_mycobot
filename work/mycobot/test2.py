from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD # When using the Raspberry Pi version of myCob
import time

PI_PORT ="/dev/ttyTHS1" 
#PI_PORT ="/dev/ttyTHS2"

# Initialize a myCobot object
mc = MyCobot(PI_PORT, PI_BAUD)
# Get the coordinates of the current location
angle_datas = mc.get_angles()
print(angle_datas)
# Pass coordinate parameters with a number of columns, let the robot arm move to the s
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
print(mc.is_paused())
# Set the wait time to ensure that the robot arm has reached the specified position
# while not mc.is_paused():
time.sleep(2.5)
# Move joint 1 to the position of 90
mc.send_angle(Angle.J1.value, 90, 50)
# Set the wait time to ensure that the robot arm has reached the specified position
time.sleep(2)
# Set the number of cycles
num = 5
# Let the robot arm swing left and right
while num > 0:
 # Move joint 2 to the position of 50
 mc.send_angle(Angle.J2.value, 50, 50)
 # Set the wait time to ensure that the robot arm has reached the specified positio
 time.sleep(1.5)
 # Move joint 2 to the position of -50
 mc.send_angle(Angle.J2.value, -50, 50)
 # Set the wait time to ensure that the robot arm has reached to the specified posi
 time.sleep(1.5)
 num -= 1
# Let the robot arm shrink. You can swing the robot arm manually and then use the get_
# Use this function to get the robot arm to where you want it to be.
# mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)
# Set the wait time to ensure that the robot arm has reached to the specified position
time.sleep(2.5)
# Release the robot arm, let
