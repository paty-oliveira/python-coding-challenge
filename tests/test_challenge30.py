import unittest
from src.challenge30 import separate_liquids


class TestChallenge30(unittest.TestCase):

    def test_should_return_a_glass_of_two_layers_with_oil_in_the_top(self):
        glass = [['W', 'W', 'W', 'W'], ['O', 'O', 'O', 'O']]
        actual_result = separate_liquids(glass)
        expected_result = [['O', 'O', 'O', 'O'], ['W', 'W', 'W', 'W']]

        self.assertEqual(expected_result, actual_result)


    def test_should_return_a_glass_of_two_layers_with_alcohol_in_the_top(self):
        glass = [['W', 'A', 'A', 'A'], ['A', 'W', 'W', 'W']]
        actual_result = separate_liquids(glass)
        expected_result = [['A', 'A', 'A', 'A'], ['W', 'W', 'W', 'W']]

        self.assertEqual(expected_result, actual_result)


    def test_should_return_a_glass_of_three_layers_with_oil_in_the_top(self):
        glass = [['H', 'H', 'W', 'O'], ['W', 'W', 'O', 'W'], ['H', 'H', 'O', 'O']]
        actual_result = separate_liquids(glass)
        expected_result = [['O', 'O', 'O', 'O'], ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_an_empty_glass(self):
        glass = []
        actual_result = separate_liquids(glass)
        expected_result = []

        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()
