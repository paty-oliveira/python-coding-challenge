import unittest
from src.challenge43 import unique_in_order


class TestChallenge43(unittest.TestCase):

    def test_should_return_empty_list_when_sequence_input_is_empty(self):
        sequence = ""
        actual_result = unique_in_order(sequence)
        expected_result = []

        self.assertListEqual(expected_result, actual_result)

    def test_should_return_exactly_the_same_sequence_when_sequence_input_not_contains_duplicate_values(self):
        sequence = "ABC"
        actual_result = unique_in_order(sequence)
        expected_result = ["A", "B", "C"]

        self.assertListEqual(expected_result, actual_result)

    def test_should_remove_duplicate_values_on_the_input_sequence_beginning(self):
        sequence = "AAB"
        actual_result = unique_in_order(sequence)
        expected_result = ["A", "B"]

        self.assertListEqual(expected_result, actual_result)

    def test_should_remove_duplicate_values_in_many_positions_of_the_input_sequence(self):
        sequence = "AAAABBBCCDAABBB"
        actual_result = unique_in_order(sequence)
        expected_result = ["A", "B", "C", "D", "A", "B"]

        self.assertListEqual(expected_result, actual_result)

    def test_should_remove_duplicates_values_in_many_positions_of_the_input_sequence_with_lower_and_upper_cases_letters(self):
        sequence = "ABBCcAD"
        actual_result = unique_in_order(sequence)
        expected_result = ['A', 'B', 'C', 'c', 'A', 'D']

        self.assertListEqual(expected_result, actual_result)

    def test_should_remove_duplicate_numbers_in_many_positions_of_the_input_sequence(self):
        sequence = [1, 2, 2, 3, 3]
        actual_result = unique_in_order(sequence)
        expected_result = [1, 2, 3]

        self.assertListEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
