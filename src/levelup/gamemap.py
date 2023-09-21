from levelup.position import Position
from levelup.controller import Direction 

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

    def calculatePosition(self,x, y, Dir):
        p=Position(x,y)
        #p = {startingPosition.xPos, startingPosition.yPos}
        
        if Dir ==Direction.NORTH:
            p.yPos=p.yPos+1
        elif Dir ==Direction.SOUTH:
            p.yPos=p.yPos-1
        elif Dir ==Direction.EAST:
            p.xPos=p.xPos+1
        elif Dir ==Direction.WEST:
            p.xPos=p.xPos-1
        else:
            pass

        return(p)

        