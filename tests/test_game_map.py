from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.controller import Direction
from levelup.position import Position

class TestGameMap(TestCase):
    def test_init(self):
        gm = GameMap(100)
        self.assertEqual(100, gm.numPositions)
        

    def test_getPositions(self):
        gm = GameMap(100)
        self.assertEqual(list(), gm.get_positions())

    def test_calculatePositionNorth(self):
        gm = GameMap(100)
        
        p2 = gm.calculatePosition(5,5, Direction.NORTH)
        
        p=Position(5,6)
        self.assertEqual(p2.yPos,p.yPos)

    def test_calculatePositionSouth(self):
        gm = GameMap(100)
        
        p2 = gm.calculatePosition(5,5, Direction.SOUTH)
        
        p=Position(5,4)
        self.assertEqual(p2.yPos,p.yPos)

    def test_calculatePositionEast(self):
        gm = GameMap(100)
        
        p2 = gm.calculatePosition(5,5, Direction.EAST)
        
        p=Position(6,5)
        self.assertEqual(p2.yPos,p.yPos)

    def test_calculatePositionWest(self):
        gm = GameMap(100)
        
        p2 = gm.calculatePosition(5,5, Direction.WEST)
        
        p=Position(4,5)
        self.assertEqual(p2.yPos,p.yPos)