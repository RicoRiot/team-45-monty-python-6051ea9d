from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        coordubates = position(0,0)
        self.assertEqual(coordinates,{"x":0,"y":0})