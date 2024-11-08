from mksServoCan.mks_servo import *
from mksServoCan.mks_enums import *
import can

from helper import *
from defines import *



controlBus = can.interface.Bus(
    bustype="slcan", channel="/dev/tty.usbmodem206A38584D4D1", bitrate=500000
)
notifier = can.Notifier(controlBus, [])


x_servo = MksServo(controlBus, notifier, 3)

servos = {}

servos["x"] = x_servo

#servos["x"].set_limit_port_remap(Enable.Enable)
servos["x"].run_motor_relative_motion_by_pulses(Direction.CW, 400, 10, 20)


