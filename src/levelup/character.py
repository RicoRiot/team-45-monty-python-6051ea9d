from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

class Character:
    name = ""
    default_position_x = -100
    default_position_y = -100
    current_position=Position(default_position_x, default_position_y)
    move_count=0

    def __init__(self, character_name):
        self.name = character_name
        self.move_count=0

    def get_position(self):
        return self.current_position

    def enter_map(self, m):
        self.current_position.x_pos = m.starting_position.x_pos
        self.current_position.y_pos = m.starting_position.y_pos

    def move(self, DIRECTION):
        self.current_position=GameMap.calculate_position(self.current_position.x_pos, self.current_position.y_pos, Direction.NORTH)
        move_count+=1


    
    