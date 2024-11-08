from mksServoCan.mks_servo import *
from mksServoCan.mks_enums import *
import can

from helper import *
from defines import *

controlBus = can.interface.Bus(
    bustype="slcan", channel="/dev/tty.usbmodem206A38584D4D1", bitrate=500000
)
notifier = can.Notifier(controlBus, [])

servos = {}
axis_map = [X, Y, Z, A, B, C]

for id, axis in enumerate(axis_map):
    servos[axis] = MksServo(controlBus, notifier, id+1)
    

for axis in [Y, Z]:
    servos[axis].nb_go_home()
    


    

while False:
    for axis in [Y, Z]:
        servos[axis].run_motor_in_speed_mode(Direction.CCW, 1000, 100)
    break
            


    



