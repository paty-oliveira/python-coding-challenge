import unittest
from src.challenge45 import move_zeros


class TestChallenge45(unittest.TestCase):

    def test_should_move_zero_to_the_end(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        )

        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

        self.assertEqual(move_zeros([0, 0]), [0, 0])

        self.assertEqual(move_zeros([0]), [0])

        self.assertEqual(move_zeros([]), [])


if __name__ == '__main__':
    unittest.main()
