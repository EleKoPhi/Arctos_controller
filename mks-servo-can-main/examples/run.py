import can
import time
import mks_servo
from mks_servo import MksServo

import logging

# Stock slcan firmware on Windows
bus = can.interface.Bus(
    bustype="slcan", channel="/dev/tty.usbmodem206A38584D4D1", bitrate=500000
)
notifier = can.Notifier(bus, [])


def wait_for_motor_idle2(axis: MksServo, timeout):
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time < timeout) and axis.is_motor_running():
        print(axis.read_motor_speed(), flush=True)
        time.sleep(0.1)  # Small sleep to prevent busy waiting
    return axis.is_motor_running()


# class ServoAxis(Enum):
#    ServoX = 0,
#    ServoY = 1
def move_motor(axis: MksServo, absolute_position):
    print(f"Moving motor to absolute position {absolute_position}", flush=True)
    print(
        axis.run_motor_absolute_motion_by_axis(1000, 250, absolute_position), flush=True
    )
    wait_for_motor_idle2(axis, 30)
    value = axis.read_encoder_value_addition()  # ['value']
    error = absolute_position - value
    print(f"Movement at {absolute_position} with error {error}")
    print(f"", flush=True)
    print()


from .mks_enums import *


def move_motor_in_speedMode(axis: MksServo, dir, speed):
    axis.run_motor_in_speed_mode(dir, speed, 240)
    return True

    while False:
        status = servo.query_motor_status()
        # print(servo.read_encoder_value_carry())
        print(servo.read_encoder_value_addition())

        # Check if the status is MotorStop
        if status["status"] == MksServo.MotorStatus.MotorStop:
            print("Motor has stopped.", flush=True)
            break

        # Wait for 100 ms
        time.sleep(0.1)


x_servo = MksServo(bus, notifier, 2)
y_servo = MksServo(bus, notifier, 1)
z_servo = MksServo(bus, notifier, 3)
a_servo = MksServo(bus, notifier, 4)
b_servo = MksServo(bus, notifier, 5)
c_servo = MksServo(bus, notifier, 6)

servos = {}

servos["x"] = x_servo
servos["y"] = y_servo
servos["z"] = z_servo
servos["a"] = a_servo
servos["b"] = b_servo
servos["c"] = c_servo

"""for servo_key in servos.keys():
    servos[servo_key].emergency_stop_motor()
    servos[servo_key].set_subdivisions(128)
    servos[servo_key].set_working_current(2000)
    servos[servo_key].set_current_axis_to_zero()"""

"""while True:
    move_motor_in_speedMode(servos["x"],Direction.CCW)
    time.sleep(2)
    move_motor_in_speedMode(servos["x"],Direction.CW)
    time.sleep(2)
    #for servo_key in servos.keys():
     #   move_motor(servos[servo_key], 0)
    #    move_motor(servos[servo_key], 0x1000 * 16)
    #   time.sleep(1)"""

# Importieren der Pygame-Bibliothek
import pygame

pygame.init()
pygame.display.set_mode((480, 480))
pygame.display.set_caption("Arctos Controller")
spielaktiv = True
speed = 0
speed_y = 0
servos["x"].set_subdivisions(128)
# Schleife Hauptprogramm
x = 0
y = 0
x, y = pygame.mouse.get_pos()


def definePos(value):
    if value > 240 + 40:
        return "R"
    if value < 240 - 40:
        return "L"
    else:
        return "N"


servos["x"].set_working_current(1000)
servos["x"].set_subdivisions(254)
start = False

surface = pygame.display.set_mode((480, 480))
surface.fill((255, 0, 0))
pygame.display.flip()
while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start = True
                surface.fill((0, 255, 0))
                pygame.display.flip()
            if event.key == pygame.K_q:
                start = False
                surface.fill((255, 0, 0))
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                servos["x"].set_current_axis_to_zero()
            if event.key == pygame.K_LEFT:
                move_motor(servos["x"], 0x100 * 255)
            if event.key == pygame.K_RIGHT:
                move_motor(servos["x"], 0)
            

    pygame.mouse.get_pos()
    x, y = pygame.mouse.get_pos()
    print("x" + str(x))
    print("y" + str(y))

    old_speed = 0
    new_speed = 0
    first_run = True

    cnt_x = definePos(x)
    if cnt_x == "R" and start:
        new_speed = int(200 * ((x - 280) / 200))
        print()
        move_motor_in_speedMode(servos["x"], Direction.CCW, max(new_speed, 500))
    elif cnt_x == "L" and start:
        new_speed = int(200 * (((200 - x) / 200)))
        move_motor_in_speedMode(servos["x"], Direction.CW, max(new_speed, 500))
    else:
        move_motor_in_speedMode(servos["x"], Direction.CW, 0)

    cnt_y = definePos(y)
    print(y)
    if cnt_y == "R" and start:
        move_motor_in_speedMode(
            servos["y"], Direction.CCW, int(300 * ((y - 280) / 200))
        )
    elif cnt_y == "L" and start:
        new_speed = int(300 * (((200 - y) / 200)))
        if new_speed > old_speed + 30 or new_speed < old_speed + 30:
            move_motor_in_speedMode(
                servos["y"], Direction.CW, int(300 * (((200 - y) / 200)))
            )
            old_speed = new_speed
        else:
            None
    else:
        move_motor_in_speedMode(servos["y"], Direction.CW, 0)

    # time.sleep(0.05)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_motor_in_speedMode(servos["x"], Direction.CCW, 10)
            if event.key == pygame.K_RIGHT:
                move_motor_in_speedMode(servos["x"], Direction.CW, 10)
        #        if event.key == pygame.K_UP:
        #            move_motor_in_speedMode(servos["y"], Direction.CCW, 10)
        #        if event.key == pygame.K_DOWN:
        #           move_motor_in_speedMode(servos["y"], Direction.CW, 10)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_motor_in_speedMode(servos["x"], Direction.CCW, 0)
                speed = 0
            if event.key == pygame.K_RIGHT:
                move_motor_in_speedMode(servos["x"], Direction.CW, 0)
                speed = 0
            if event.key == pygame.K_UP:
                move_motor_in_speedMode(servos["y"], Direction.CCW, 0)
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
                move_motor_in_speedMode(servos["y"], Direction.CW, 0)

    keys = pygame.key.get_pressed()

    """if keys[pygame.K_LEFT]:
        speed += 25
        move_motor_in_speedMode(servos["x"], Direction.CCW, 10 + min(speed, 1000))
    if keys[pygame.K_RIGHT]:
        speed += 25
        move_motor_in_speedMode(servos["x"], Direction.CW, 10 + min(speed, 1000))
    if keys[pygame.K_UP]:
        speed_y += 5
        move_motor_in_speedMode(servos["y"], Direction.CCW, 10 + min(speed_y, 200))
    if keys[pygame.K_DOWN]:
        speed_y += 5
        move_motor_in_speedMode(servos["y"], Direction.CW, 10 + min(speed_y, 200))"""

    time.sleep(0.1)


exit()
# print(servo.set_work_mode(MksServo.WorkMode.SrvFoc))

# if not servo.b_calibrate_encoder()['status'] == MksServo.CalibrationResult.CalibratedSuccess:
#   logging.error("Calibration failed")

print(a_servo.emergency_stop_motor())

print(a_servo.set_work_mode(MksServo.WorkMode.SrvFoc))
print(a_servo.set_subdivisions(16))
print(a_servo.set_working_current(2000))
# print(servo.release_motor_shaft_locked_protection_state())
# print(servo.set_current_axis_to_zero())

while True:
    try:
        move_motor(z_servo, 0x1000 * 13)
        # move_motor(y_servo, 0x1000 * 13)
        move_motor(z_servo, 0 * 13)
        # move_motor(y_servo, 0x0 * 13)
    except:
        None


# print(servo.run_motor_relative_motion_by_pulses(MksServo.Direction.CW, 50, 1, 0x000A000))
# print(servo.run_motor_absolute_motion_by_pulses(400, 2, 0x0FA00))

move_motor(0x4000)
move_motor(-0x4000)
move_motor(0x4000)

asd

# Test command 01:
print("---- 5.1.1 Read the encoder value (carry)----")
print(servo.read_encoder_value_carry())

print("---- 5.1.2 Read the encoder value (addition) ----")
print(servo.read_encoder_value_addition())

print("---- 5.1.3 Read the real-time speed of the motor ----")
print(servo.read_motor_speed())

print("---- 5.1.4 Read the number of pulses received ----")
print(servo.read_num_pulses_received())

print("---- 5.1.5 Read the IO Ports status ----")
print(servo.read_io_port_status())

print("---- 5.1.6 Read the error of the motor shaft angle ----")
print(servo.read_motor_shaft_angle_error())

print("---- 5.1.7 Read the En pins status ----")
print(servo.read_en_pins_status())

print("---- 5.1.8 Read the go back to zero status when power on ----")
print(servo.read_go_back_to_zero_status_when_power_on())

print("---- 5.1.9 Release the motor shaft locked-rotor protection state ----")
print(servo.release_motor_shaft_locked_protection_state())

print("---- 5.1.10 Read the motor shaft protection state ----")
print(servo.read_motor_shaft_protection_state())

print("---- 5.2.1 Calibrate the encoder ----")
# print(servo.calibrate_encoder())

print("---- 5.2.2 Set the work mode ----")
print(servo.set_work_mode(MksServo.WorkMode.SrOpen))

print("---- 5.2.3 Set the working current ----")
print(servo.set_working_current(1000))

print("---- 5.2.4 Set the holding current percentage ----")
# print(servo.set_holding_current(MksServo.HoldingStrength.FIFTHTY_PERCENT))

print("---- 5.2.5 Set subdivision ----")
# print(servo.set_subdivision(4))

print("---- 5.2.6 Set the active of the En pin ----")
print(servo.set_en_pin_config(MksServo.EnPinEnable.ActiveHigh))

print("---- 5.2.7 Set the direction of motor rotation ----")
print(servo.set_motor_rotation_direction(MksServo.Direction.CW))

print("---- 5.2.8 Set auto turn off the screen function ----")
print(servo.set_auto_turn_off_screen(MksServo.Enable.Disabled))

print("---- 5.2.9 Set the motor shaft locked-rotor protection function ----")
print(servo.set_motor_shaft_locked_rotor_protection(MksServo.Enable.Enabled))

print("---- 5.2.10 Set the subdivision interpolation function ----")
# print(servo.set_subdivision_interpolation(MksServo.Enable.Enabled))

print("---- 5.2.11 Set the CAN bitRate ----")
print(servo.set_can_bitrate(MksServo.CanBitrate.Rate500K))

print("---- 5.2.12 Set the CAN ID  ----")
print(servo.set_can_id(1))

print("---- 5.2.13 Set the slave respond and active  ----")
# print(servo.set_slave_respond_active())

print("---- 5.2.14 Set the key lock or unlock ----")
print(servo.set_key_lock_enable(MksServo.Enable.Disabled))

print("---- 5.2.15 Set the group ID  ----")
print(servo.set_group_id(0))


print("---- 5.3.1 Set the parameter of home ----")
# print(servo.set_home(MksServo.EndStopLevel.High, MksServo.Direction.CW, 5, MksServo.Enable.Enabled))

print("---- 5.3.2 Go home ----")
print(servo.go_home())

print("---- 5.3.3 Set Current Axis to Zero ----")
# print(servo.set_current_axis_to_zero())

print("---- 5.3.4 Set limit port remap ----")
# print(servo.set_limit_port_remap(MksServo.Enable.Enabled))

print("---- 5.4 Set the parameter of 0_mode ----")
# print(servo.set_mode0(MksServo.Mode0.NearMode, MksServo.Enable.Enabled, MksServo.Direction.CW))

print("---- 5.5 Restore the default parameter ----")
print(servo.restore_default_parameters())


print("---- 6.2.1 Query the motor status ----")
print(servo.query_motor_status())

print("---- 6.2.2 Enable motor command ----")
print(servo.enable_motor(True))

print("---- 6.2.3 Emergency stop the motor ----")
# print(servo.emergency_stop_motor())

print("---- 6.4.1 Speed mode command ----")
# print(run_motor_speed_mode(Direction.CW, 320, 2))

print("---- 6.4.3 Save/Clean the parameter in speed mode  ----")
# print(servo.save_clean_in_speed_mode(MksServo.SaveCleanState.Clean))

print("---- 6.5.1 position mode1: relative motion by pulses ----")
print(
    servo.run_motor_relative_motion_by_pulses(MksServo.Direction.CW, 200, 1, 0x055A000)
)

print("---- 6.6.1 Position mode 2: absolute motion by pulses ----")
# print(servo.run_motor_absolute_motion_by_pulses(400, 2, 0x0FA00))

print("---- 6.7.1 Position mode 3: relative motion by axis ----")
# print(servo.run_motor_relative_motion_by_axis())

print("---- 6.8.1 Position mode 4: Absolute motion by axis ----")
# print(servo.run_motor_absolute_motion_by_axis())


# def get_servo(id, value):
#    if id == ServoAxis.ServoX:
#       return servo
#    elif id == ServoAxis.ServoY:
#        return servo_y
#
# def move_motor(id, value):
#    selected_servo = get_servo(id)
#    print(selected_servo.run_motor_relative_motion_by_pulses(MksServo.Direction.CW, 400, 1, 0x000A000))
#
#    while True:
#        status = servo.query_motor_status()
#        print(status, flush=True)
#
#        # Check if the status is MotorStop
#        if status['status'] == MksServo.MotorStatus.MotorStop:
#            print("Motor has stopped.")
#            break


def move_motors(x, y):
    return 1


while True:
    status = servo.query_motor_status()
    print(status, flush=True)

    # Check if the status is MotorStop
    if status["status"] == MksServo.MotorStatus.MotorStop:
        print("Motor has stopped.")
        break

    # Wait for 100 ms
    time.sleep(0.1)
notifier.stop()
bus.shutdown()
