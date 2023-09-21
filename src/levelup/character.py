from levelup.gamemap import GameMap

class Character:
    name = ""
    current_position = [-100, -100]
    move_count=0

    def __init__(self, character_name):
        self.name = character_name
        self.move_count=0

    def get_position(self):
        return self.current_position

    def enter_map(self, m):
        self.current_position = m.startingPosition

    def move(self, DIRECTION):
        current_position=GameMap.CalculatePosition(current_position, DIRECTION)
        self.move_count+=1



    
    