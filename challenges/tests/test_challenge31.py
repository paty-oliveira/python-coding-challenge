import unittest
from src.challenge31 import compare


class TestChallenge31(unittest.TestCase):

    def test_should_return_true_when_the_second_input_is_the_duplication_representation_of_the_first(self):
        list1 = [2, 4, 6]
        list2 = [4, 16, 36]
        actual_result = compare(list1, list2)
        self.assertTrue(actual_result)

    def test_should_return_false_when_the_second_input_is_not_the_duplication_representation_of_the_first(self):
        list1 = [121, 144, 19, 161, 19, 144, 19, 11]
        list2 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
        actual_result = compare(list1, list2)
        self.assertFalse(actual_result)


if __name__ == '__main__':
    unittest.main()
