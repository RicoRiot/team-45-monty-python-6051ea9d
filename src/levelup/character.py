class Character:
    name = ""
    current_position = [-100, -100]

    def __init__(self, character_name):
        self.name = character_name

    def get_position(self):
        return self.current_position

    def enter_map(self, m):
        self.current_position = m.startingPosition
