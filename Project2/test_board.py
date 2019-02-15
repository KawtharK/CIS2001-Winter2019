from unittest import TestCase
from Checkers import *

class TestBoard(TestCase):
    def test_num_jumps(self):
        expected_jumps = 3

        board = Board()
        board.add_checker(Board.WHITE, 4, 3)
        board.add_checker(Board.BLACK, 1, 2)
        board.add_checker(Board.BLACK, 1, 4)
        board.add_checker(Board.BLACK, 1, 6)
        board.add_checker(Board.BLACK, 3, 4)

        actual_jumps = board.num_jumps(4,3)

        self.assertEqual(expected_jumps, actual_jumps)


