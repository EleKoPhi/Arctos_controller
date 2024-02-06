from defines import gearBoxRatios


class Gearbox:
    def __init__(self, ratio) -> None:
        self.ratio = ratio

    def __str__(self):
        return "Gearbox with {} ratio".format(self.ratio)


if "__main__" == __name__:
    x_gearBox = Gearbox(gearBoxRatios.X)
