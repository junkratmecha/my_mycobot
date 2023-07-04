from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD # When using the Raspberry Pi version of myCob
import time

# for mypalletizer
# from pymycobot import MyPalletizer

# for MechArm
# from pymycobot import MechArm

PI_PORT ="/dev/ttyTHS1" 
#PI_PORT ="/dev/ttyTHS2"

# Initialize a myCobot object
mc = MyCobot(PI_PORT, PI_BAUD)
# mc = MyPalletizer("com10",115200)
# mc = MechArm("com10",115200)

print(mc.get_angles())