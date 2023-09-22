from levelup.position import Position
from levelup.controller import Direction

class GameMap:
    num_positions = 0
   #all_positions = list()
    starting_position = Position

    def __init__(self, positions):
        self.starting_position = Position(0,0)
        self.num_positions = positions
        self.all_positions = list()

    def get_positions(self):
        return self.all_positions

    def calculate_position(self,x, y, move_direction):
        p=Position(x,y)
        #p = {starting_position.x_pos, starting_position.y_pos}
        print (move_direction)
        if move_direction == "n": #Direction.NORTH:
            p.y_pos=p.y_pos+1
        elif move_direction ==Direction.SOUTH:
            p.y_pos=p.y_pos-1
        elif move_direction ==Direction.EAST:
            p.x_pos=p.x_pos+1
        elif move_direction ==Direction.WEST:
            p.x_pos=p.x_pos-1
        else:
            pass

        return(p)

    def is_position_valid(self,position_x, position_y):
        if position_x>9:
           return False
        elif position_x<0:
            return False
        elif position_y>9:
            return False
        elif position_y<0:
            return False
        else:
            return True


    