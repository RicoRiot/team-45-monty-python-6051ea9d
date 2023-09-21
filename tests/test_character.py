from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_position(self):
        expected_position = [4, 7]
        testobj = Character("Trogdor")
        testobj.current_position=expected_position
        actual_position=testobj.get_position()
        self.assertEqual(expected_position, actual_position)
        
    def test_enter_map(self):
        test_character = Character("Trogdor")
        start_position = [0,0]
        testmap = GameMap(100)
        testmap.startingPosition = start_position
        test_character.enter_map(testmap)
        self.assertEqual(start_position, test_character.current_position)

    def test_move_count_increment(self):
        pass

    def test_move_north(self):
        test_character = Character("Sir Robyn")
        test_character.current_position = {5,5}
        test_character.move_count=8
        expected_position={5,6}
        expected_move_count=9
        test_character.move("n")
        self.assertEqual(expected_move_count, test_character.move_count)
        self.assertEqual(expected_position, test_character.current_position)

