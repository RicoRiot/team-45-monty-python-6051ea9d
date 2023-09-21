from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        test_coordinate=Position(0,0)
        self.assertEqual({0,0},test_coordinate.coordinates )

        test_coordinate = Position(3,4)
        self.assertEqual({3,4}, test_coordinate.coordinates)
