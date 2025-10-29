import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_value_not_found(self):
        values = [1, 5, 19, 41, 50, 67]
        value = 9

        actual_result = binary_search(values, value)
        self.assertFalse(actual_result)

    def test_value_found(self):
        values = [1, 5, 19, 41, 50, 67]
        value = 1

        actual_result = binary_search(values, value)
        self.assertTrue(actual_result)


if __name__ == "__main__":
    unittest.main()
