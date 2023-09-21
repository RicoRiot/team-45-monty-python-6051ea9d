from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_position(self):
        expected_position = {4, 7}
        testobj = Character("Trogdor")
        testobj.current_position=expected_position
        actual_position=testobj.get_position()
        self.assertEqual(expected_position, actual_position)
        
