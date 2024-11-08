from Gearbox import Gearbox
from Motor import Motor
from defines import MotorSetting
from mksServoCan.mks_enums import WorkMode, Direction

import time


class Axis:
    def __init__(
        self,
        gearBox: Gearbox,
        motors: list[Motor],
        motorArrangement: MotorSetting = MotorSetting.Parallel,
    ) -> None:
        self.gearBox = gearBox
        self.motors = []
        if type(motors) != list:
            self.motors.append(motors)
        else:
            self.motors = motors

        self.directionFactor = (
            [1, 1] if motorArrangement == MotorSetting.Parallel else [1, -1]
        )

        self.x1 = None
        self.y1 = None
        self.z1 = None
        self.degree = None
        self.x2 = None
        self.y2 = None
        self.z2 = None

    def moveAxis(self, degree: int):
        for index, motor in enumerate(self.motors):
            motor.run_n_MotorTurns(
                self.gearBox.ratio * (degree / 360) * self.directionFactor[index]
            )

    def setSpeed(self, speed: int):
        for motor in self.motors:
            motor.speed = speed

    def setAcceleration(self, acceleration: int):
        for motor in self.motors:
            motor.acceleration = acceleration

    def home(self):
        for motor in self.motors:
            motor.nb_go_home()
        self.degree = 0

    def getPorts(self):
        print(self.motors[0].read_encoder_value_carry())
        time.sleep(0.1)

    def setWorkMode(self, workMode: WorkMode):
        for motor in self.motors:
            motor.set_work_mode(workMode)

    def moveAxis(self, speed, direction: Direction):
        for motor in self.motors:
            try:
                motor.run_motor_in_speed_mode(direction, speed, 200)
            except:
                None

    def __str__(self):
        return str(self.motor.ID)
