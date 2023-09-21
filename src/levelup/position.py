class Position:
    xPos = -1
    yPos = -1
    coordinates = {"x":xPos,"y":yPos}

    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.coodinates.update({"x":x,"y":y})
