from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.controller import Direction
from levelup.position import Position

class TestGameMap(TestCase):
    def test_init(self):
        gm = GameMap(100)
        self.assertEqual(100, gm.num_positions)
        

    def test_getPositions(self):
        gm = GameMap(100)
        self.assertEqual(list(), gm.get_positions())

    def test_calculate_position_north(self):
        gm = GameMap(100)
        
        p2 = gm.calculate_position(5,5, "n")
        
        p = Position(5, 6) 
        self.assertEqual(p2.y_pos,p.y_pos)

    def test_calculate_position_south(self):
        gm = GameMap(100)
        
        p2 = gm.calculate_position(5,5, Direction.SOUTH)
        
        p=Position(5,4)
        self.assertEqual(p2.y_pos,p.y_pos)

    def test_calculate_position_east(self):
        gm = GameMap(100)
        
        p2 = gm.calculate_position(5,5, Direction.EAST)
        
        p=Position(6,5)
        self.assertEqual(p2.y_pos,p.y_pos)

    def test_calculate_position_west(self):
        gm = GameMap(100)
        
        p2 = gm.calculate_position(5,5, Direction.WEST)
        
        p=Position(4,5)
        self.assertEqual(p2.y_pos,p.y_pos)


    def test_is_position_valid (self):
        gm = GameMap(100)
        ASSERT_FALSE=False
        pos = Position(-1, -1)
        self.assertEqual(gm.is_position_valid(pos.x_pos, pos.y_pos), ASSERT_FALSE)