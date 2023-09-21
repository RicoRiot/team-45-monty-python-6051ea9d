from unittest import TestCase
from levelup.gamemap import GameMap

class TestGameMap(TestCase):
    def test_init(self):
        gm = GameMap(100)
        self.assertEqual(100, gm.numPositions)
        

    def test_getPositions(self):
        gm = GameMap(100)
        self.assertEqual(list(), gm.get_positions())