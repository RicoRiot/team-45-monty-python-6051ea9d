from unittest import TestCase
from levelup.gamemap import GameMap

class TestGameMap(TestCase):
    def test_init(self):
        gm = GameMap(100)
        self.assertEqual(100, gm.numPositions)
        

