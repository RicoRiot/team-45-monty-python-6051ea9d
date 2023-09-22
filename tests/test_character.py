from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_position(self):
        expected_position = Position(4,7)
        testobj = Character("Trogdor")
        testobj.current_position=expected_position
        actual_position=testobj.get_position()
        self.assertEqual(expected_position, actual_position)
        
    def test_enter_map(self):
        test_character = Character("Trogdor")
        start_position = Position(0,0)
        testmap = GameMap(100)
        testmap.starting_position = start_position
        test_character.enter_map(testmap)
        self.assertEqual(start_position.x_pos, test_character.current_position.x_pos)
        self.assertEqual(start_position.y_pos, test_character.current_position.y_pos)

    def test_move_count_increment(self):
        pass

    def test_move_north(self):
        test_character = Character("Sir Robyn")
        test_character.current_position.x_pos=5
        test_character.current_position.y_pos=5
        test_character.move_count=8
        expected_x_position=5
        expected_y_position=6
        expected_position=Position(expected_x_position, expected_y_position)
        expected_move_count=9
        test_character.move(Direction.NORTH)
        self.assertEqual(test_character.current_position.x_pos, expected_position.x_pos)
        self.assertEqual(test_character.current_position.y_pos, expected_position.y_pos)

