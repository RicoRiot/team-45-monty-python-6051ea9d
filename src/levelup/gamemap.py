from levelup.position import Position
from levelup.controller import Direction 

class GameMap:
    num_positions = 0
   all_positions = list()
    starting_position = Position

    def __init__(self, positions):
        self.starting_position = Position(0,0)
        self.num_positions = positions
        self.all_positions = list()

    def get_positions(self):
        return self.all_positions

    def calculate_position(self,x, y, Dir):
        p=Position(x,y)
        #p = {starting_position.x_pos, starting_position.y_pos}
        
        if Dir ==Direction.NORTH:
            p.y_pos=p.y_pos+1
        elif Dir ==Direction.SOUTH:
            p.y_pos=p.y_pos-1
        elif Dir ==Direction.EAST:
            p.x_pos=p.x_pos+1
        elif Dir ==Direction.WEST:
            p.x_pos=p.x_pos-1
        else:
            pass

        return(p)

        def is_position_valid(self,pos):
            if pos.x_pos>9:
                return False
            elif pos.x_pos<0:
                return False
            elif pos.y_pos>9:
                return False
            elif pos.y_pos<0:
                return False
            else:
                return True


        