class Position:
    xPos = -1
    yPos = -1
    coordinates = {xPos,yPos}

    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.coordinates={self.xPos, self.yPos}
        #self.coordinates.update({"x":x,"y":y})
        #return [self.xPos, self.yPos]
