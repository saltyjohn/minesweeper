import unittest

from components.MineSquare import MineSquare


# Pointless, but using to build a testing folder
class Test_MineSquare_Properties(unittest.TestCase):
    def setUp(self):
        self.mine_square = MineSquare(True, 1)
        self.not_mine_square = MineSquare(False, 0)
        self.flag_mine_square = MineSquare(False, 0)

    def test_is_mine(self):
        self.assertTrue(self.mine_square.is_mine)
        self.assertFalse(self.not_mine_square.is_mine)

    def test_neighbor_count(self):
        self.assertEqual(self.mine_square.neighbor_count, 1)
        self.assertEqual(self.not_mine_square.neighbor_count, 0)

    def test_display_char(self):
        self.assertEqual(self.mine_square.display_char, "#")
        self.assertEqual(self.not_mine_square.display_char, "#")

    def test_update_char(self):
        self.mine_square.update_char()
        self.not_mine_square.update_char()
        self.flag_mine_square.update_char(flag=True)

        self.assertEqual(self.mine_square.display_char, "*")
        self.assertEqual(self.not_mine_square.display_char, "0")
        self.assertEqual(self.flag_mine_square.display_char, "!")


if __name__ == "__main__":
    unittest.main()
