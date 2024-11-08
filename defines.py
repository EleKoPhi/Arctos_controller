X = "x"
Y = "y"
Z = "z"
A = "a"
B = "b"
C = "c"

revolution = 0x4000

reductionRatios = {}
reductionRatios[X] = 13.5
reductionRatios[Y] = 150
reductionRatios[Z] = 150
reductionRatios[A] = 48
reductionRatios[B] = 67.82
reductionRatios[C] = 67.82


from enum import Enum


class AxisId(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"
    A = "A"
    B = "B"
    C = "C"

    def getIds():
        return [AxisId.X, AxisId.Y, AxisId.Z, AxisId.A, AxisId.B, AxisId.C]


class MotorIDs:
    IDs = [1, 2, 3, 4, 5, 6]

    IdAxisMap = {
        AxisId.X: 2,
        AxisId.Y: 1,
        AxisId.Z: 3,
        AxisId.A: 4,
        AxisId.B: [5, 6],
        AxisId.C: [5, 6],
    }

    def idToMotorType(id):
        if id == 1 or id == 2:
            return MotorType.MKS57
        else:
            return MotorType.MKS42


class EndStopOffset:
    offset = {AxisId.X: -123}


class gearBoxRatios:
    ratios = {}
    ratios[AxisId.X] = 13.50
    ratios[AxisId.Y] = 150.00
    ratios[AxisId.Z] = 150.00
    ratios[AxisId.A] = 48.00
    ratios[AxisId.B] = 67.82
    ratios[AxisId.C] = 67.82


class MotorType(Enum):
    MKS42 = 0
    MKS57 = 1


class MotorSetting:
    Parallel = 0
    Inverse = 1

    Mapping = {}
    Mapping[AxisId.X] = Parallel
    Mapping[AxisId.Y] = Parallel
    Mapping[AxisId.Z] = Parallel
    Mapping[AxisId.A] = Parallel
    Mapping[AxisId.B] = Parallel
    Mapping[AxisId.C] = Inverse


class DefaultMotorSettings:
    SUBDIVISION = 16
    WORKINGCURRENT = {}
    WORKINGCURRENT[MotorType.MKS42] = 1600
    WORKINGCURRENT[MotorType.MKS57] = 3200


class canDefines:
    TYPE = "slcan"
    CHANNEL = "/dev/tty.usbmodem206A38584D4D1"
    BITRATE = 500000
