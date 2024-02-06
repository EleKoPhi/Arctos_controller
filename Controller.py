import can
from defines import *


class Controller:
    def __init__(self, bustype: str, channel: str, bitrate: int) -> None:
        self.controlBus = can.interface.Bus(
            bustype=bustype, channel=channel, bitrate=bitrate
        )
        self.notifier = can.Notifier(self.controlBus, [])

    def __del__(self):
        self.controlBus.shutdown()


if "__main__" == __name__:
    c = Controller(canDefines.TYPE, canDefines.CHANNEL, canDefines.BITRATE)
