from pymycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
# シリアルポートとボーレートを設定します (これらは環境によって異なります)
PI_PORT ="/dev/ttyTHS1" 

# MyCobotオブジェクトを作成します
mc = MyCobot(PI_PORT, PI_BAUD)

# 全てのサーボのトルクをオフにします
mc.release_servo(2)
# for servo_id in range(0, 7):
#     mc.release_servo(servo_id)