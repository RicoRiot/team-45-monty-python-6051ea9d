from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        test_x_pos = 0
        test_y_pos = 0
        test_position = Position(test_x_pos,test_y_pos)

        self.assertEqual(0,test_position.x_pos)
        self.assertEqual(0,test_position.y_pos)
