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

        self.Axis = {}
        self.motors = {}
        for id in MotorIDs.IDs:
            self.motors[id] = Motor(self.controller, id, MotorIDs.idToMotorType(id))

        for axisId in AxisId.getIds():
            self.Axis[axisId] = Axis(
                Gearbox(gearBoxRatios.ratios[axisId]),
                getObjectsFromDict(self.motors, MotorIDs.IdAxisMap[axisId]),
                MotorSetting.Mapping[axisId],
            )

    def __del__(self):
        None


gain = -2

test_x = False
test_y = False
test_z = False
test_a = True

#if "__main__" == __name__:
#    arctos = Arctos()
#    gain = -1
#    while True:
#        if test_x:
#            arctos.Axis[AxisId.X].setSpeed(200)
#            arctos.Axis[AxisId.X].setAcceleration(100)
#            arctos.Axis[AxisId.X].moveAxis(90 * gain)
#        if test_y:
#            arctos.Axis[AxisId.Y].setSpeed(400)
#            arctos.Axis[AxisId.Y].setAcceleration(100)
#            arctos.Axis[AxisId.Y].moveAxis(50 * gain)
#        if test_z:
#            arctos.Axis[AxisId.Z].setSpeed(400)
#            arctos.Axis[AxisId.Z].setAcceleration(100)
#            arctos.Axis[AxisId.Z].moveAxis(60 * gain)
#        if test_a:
#            arctos.Axis[AxisId.A].setSpeed(400)
#            arctos.Axis[AxisId.A].setAcceleration(100)
#            arctos.Axis[AxisId.A].moveAxis(60 * -gain)
#        gain = gain * -1
#        time.sleep(5)
#

if "__main__" == __name__:
    arctos = Arctos()