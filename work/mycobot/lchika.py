from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
PI_PORT ="/dev/ttyTHS1" #or "/dev/ttyTHS2"
mc = MyCobot(PI_PORT, PI_BAUD)
mc.set_color(0, 0, 255)

