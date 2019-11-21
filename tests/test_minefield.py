import unittest

from components.MineField import MineField


# Pointless, but using to build a testing folder
class Test_MineField_Properties(unittest.TestCase):
    def setUp(self):
        self.minefield = MineField(0.5, 4)
        self.minefield.create_board()

    def test_density(self):
        self.assertEqual(self.minefield.density, 0.5)

    def test_size(self):
        self.assertEqual(self.minefield.size, 4)

    def test_mine_count(self):
        self.assertEqual(self.minefield.total_mines, 8)

    def test_total_sqrs(self):
        self.assertEqual(self.minefield.total_sqrs, 16)

    def test_board(self):
        self.assertTrue(len(self.minefield.board),
                        len(self.minefield.board[0]))


if __name__ == "__main__":
    unittest.main()
