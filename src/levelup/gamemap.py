class GameMap:
    numPositions = 0
    allPositions = [10][10]

    def __init__(self, positions):
        self.numPositions = positions

    def get_positions(self):
        return self.allPositions()
