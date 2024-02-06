from defines import *
from Controller import *
from Gearbox import Gearbox
from Motor import Motor
from Axis import Axis
import time

from mksServoCan.mks_enums import *


def getObjectsFromDict(_list, _id):
    returnObjects = []
    if type(_id) == list:
        for i in _id:
            returnObjects.append(_list[i])
    else:
        returnObjects = _list[_id]
    return returnObjects


class Arctos:
    def __init__(self) -> None:
        self.controller = Controller(
            canDefines.TYPE, canDefines.CHANNEL, canDefines.BITRATE
        )

        self.motors = {}
        for id in MotorIDs.IDs:
            self.motors[id] = Motor(self.controller, id, MotorIDs.idToMotorType(id))

        self.gearBoxes = {}
        for axisID in AxisIdentifiers:
            self.gearBoxes[axisID] = Gearbox(gearBoxRatios.ratios[axisID])

        self.X_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.X],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.X]),
        )
        self.Y_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.Y],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.Y]),
        )

        self.Z_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.Z],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.Z]),
        )

        self.A_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.A],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.A]),
        )

        self.B_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.B],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.B]),
        )

        self.C_Axis = Axis(
            self.gearBoxes[AxisIdentifiers.C],
            getObjectsFromDict(self.motors, MotorIDs.ID2Axis[AxisIdentifiers.C]),
            ArrangementTypes.Inverse,
        )

    def __del__(self):
        None


if "__main__" == __name__:
    arctos = Arctos()
    arctos.B_Axis.moveAxis(60)
