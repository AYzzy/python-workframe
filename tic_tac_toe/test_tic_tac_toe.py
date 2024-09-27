import unittest

from tic_tac_toe.tic_tac_toe_values import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_each_cell_are_empty(self):
        tic_tac_toe = TicTacToe()
        self.assertTrue(tic_tac_toe.tac_Tik_tac_toe_values() == [])
