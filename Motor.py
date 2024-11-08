from can import Notifier
from can.interface import Bus
from mksServoCan.mks_servo import *
from mksServoCan.mks_enums import *

from enum import Enum
from Controller import Controller
from defines import MotorType, DefaultMotorSettings


class Motor(MksServo):
    resolution = 0x4000

    def __init__(
        self,
        controller: Controller,
        id_: int,
        motorType: MotorType,
        runConfig: bool = False,
    ):
        super().__init__(controller.controlBus, controller.notifier, id_)
        if runConfig:
            self.configure(motorType)
        self.speed = 10
        self.acceleration = 100
        self.ID = id_

    def configure(self, type: MotorType):
        super().set_subdivisions(DefaultMotorSettings.SUBDIVISION)
        super().set_working_current(DefaultMotorSettings.WORKINGCURRENT[type])

    def run_n_MotorTurns(self, n: int):
        print("Run {} turns".format(n))
        super().wait_for_motor_idle(60)
        super().run_motor_relative_motion_by_axis(
            self.speed, self.acceleration, int(((0x4000) * n))
        )
