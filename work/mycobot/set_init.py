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
