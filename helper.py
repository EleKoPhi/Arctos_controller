import defines


def degreeToPos(ratio, actPosition, tarPosition):
    return (tarPosition - actPosition) * ratio


def degreeToEncodeValue(degree, ratio):
    return int((degree / 360) * defines.revolution*ratio)
