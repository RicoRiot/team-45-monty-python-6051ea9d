class GameMap:
    numPositions = 0
    allPositions = [0][0]
    startingPosition = {}

    def __init__(self, positions):
        self.numPositions = positions

    def get_positions(self):
        return self.allPositions()
