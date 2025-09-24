import unittest
from src.challenge54 import find_pair


class TestFindPair(unittest.TestCase):
    def test_example_case(self):
        values = [1, 1, 2, 2, 6, 7, 1, 2]
        target = 8
        result = find_pair(values, target)
        expected = [(1, 7), (2, 6)]
        self.assertCountEqual(result, expected)

    def test_no_pairs(self):
        values = [1, 2, 3]
        target = 10
        result = find_pair(values, target)
        self.assertEqual(result, [])

    def test_single_pair(self):
        values = [4, 5, 1]
        target = 9
        result = find_pair(values, target)
        expected = [(4, 5)]
        self.assertEqual(result, expected)

    def test_duplicate_numbers(self):
        values = [2, 2, 2, 2]
        target = 4
        result = find_pair(values, target)
        expected = [(2, 2)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
