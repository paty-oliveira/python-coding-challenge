import unittest
from src.challenge10 import flatten


class TestChallenge10(unittest.TestCase):

    def test_should_flat_two_lists_of_one_element_into_one_single_list_of_two_elements(self):
        input_param = [[1], [2]]
        current_result = flatten(input_param)
        expected_result = [1, 2]

        self.assertEqual(current_result, expected_result)

    def test_should_flat_two_list_of_two_elements_into_one_single_list_of_four_elements(self):
        input_param = [[1, 2], [3, 4]]
        current_result = flatten(input_param)
        expected_result = [1, 2, 3, 4]

        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
