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


class AxisIdentifiers(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"

    A = "A"
    B = "B"
    C = "C"


class MotorIDs:
    IDs = [1, 2, 3, 4, 5, 6]

    ID2Axis = {
        AxisIdentifiers.X: 2,
        AxisIdentifiers.Y: 1,
        AxisIdentifiers.Z: 3,
        AxisIdentifiers.A: 4,
        AxisIdentifiers.B: [5, 6],
        AxisIdentifiers.C: [5, 6],
    }

    def idToMotorType(id):
        if id == 1 or id == 2:
            return MotorType.MKS57
        else:
            return MotorType.MKS42


class gearBoxRatios:
    ratios = {}
    ratios[AxisIdentifiers.X] = 13.50
    ratios[AxisIdentifiers.Y] = 150.00
    ratios[AxisIdentifiers.Z] = 150.00
    ratios[AxisIdentifiers.A] = 48.00
    ratios[AxisIdentifiers.B] = 67.82
    ratios[AxisIdentifiers.C] = 67.82


class MotorType(Enum):
    MKS42 = 0
    MKS57 = 1


class ArrangementTypes:
    Parallel = 0
    Inverse = 1


class DefaultMotorSettings:
    SUBDIVISION = 16
    WORKINGCURRENT = {}
    WORKINGCURRENT[MotorType.MKS42] = 1600
    WORKINGCURRENT[MotorType.MKS57] = 3200


class canDefines:
    TYPE = "slcan"
    CHANNEL = "/dev/tty.usbmodem206A38584D4D1"
    BITRATE = 500000
