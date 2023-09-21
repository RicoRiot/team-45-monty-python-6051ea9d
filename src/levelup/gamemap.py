from levelup.position import Position

class GameMap:
    numPositions = 0
    allPositions = list()
    startingPosition = Position

    def __init__(self, positions):
        self.startingPosition = Position(0,0)
        self.numPositions = positions
        self.allPositions = list()

    def get_positions(self):
        return self.allPositions
