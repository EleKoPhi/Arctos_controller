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

x_servo = MksServo(controlBus, notifier, 2)
y_servo = MksServo(controlBus, notifier, 1)
z_servo = MksServo(controlBus, notifier, 3)
a_servo = MksServo(controlBus, notifier, 4)
b_servo = MksServo(controlBus, notifier, 5)
c_servo = MksServo(controlBus, notifier, 6)

servos["x"] = x_servo
servos["y"] = y_servo
servos["z"] = z_servo
servos["a"] = a_servo
servos["b"] = b_servo
servos["c"] = c_servo

servos[C].set_subdivisions(16)
servos[C].set_working_current(1000)
servos[B].set_subdivisions(16)
servos[B].set_working_current(1000)
# servos[X].set_current_axis_to_zero()
#
# servos[X].run_motor_absolute_motion_by_axis(
#    50, 1, degreeToEncodeValue(-90, reductionRatios[X])
# )

servos[A].run_motor_in_speed_mode(Direction.CCW, 400, 1)
# servos[C].run_motor_in_speed_mode(Direction.CCW, 100, 150)

