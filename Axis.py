from Gearbox import Gearbox
from Motor import Motor
from defines import ArrangementTypes


class Axis:
    def __init__(
        self,
        gearBox: Gearbox,
        motors: list[Motor],
        motorArrangement: ArrangementTypes = ArrangementTypes.Parallel,
    ) -> None:
        self.gearBox = gearBox
        self.motors = []
        if type(motors) != list:
            self.motors.append(motors)
        else:
            self.motors = motors

        self.directionFactor = (
            [1, 1] if motorArrangement == ArrangementTypes.Parallel else [1, -1]
        )

    def moveAxis(self, degree: int):
        for index, motor in enumerate(self.motors):
            motor.run_n_MotorTurns(
                self.gearBox.ratio * (degree / 360) * self.directionFactor[index]
            )

    def __str__(self):
        return str(self.motor.ID)
