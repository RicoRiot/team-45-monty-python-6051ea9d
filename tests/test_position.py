from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        coordinates = Position(0,0)
        self.assertEqual(coordinates.coordinates,{"x":0,"y":0})