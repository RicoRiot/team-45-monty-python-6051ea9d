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
        name = character_name
        move_count=0

    def get_position(self):
        return current_position

    def enter_map(self, m):
        current_position = m.starting_position

    def move(self, DIRECTION):
        current_position=GameMap.calculate_position(current_position.x_pos, current_position.y_pos, DIRECTION)
        move_count+=1



    
    