import unittest
from src.challenge29 import to_weird_case


class TestChallenge29(unittest.TestCase):
    def test_should_return_one_word_with_even_indexed_characters_in_upper_case(self):
        input_word = "test"
        actual_result = to_weird_case(input_word)
        expected_result = "TeSt"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_two_words_with_even_indexed_characters_in_upper_case(self):
        input_word = "Weird string"
        actual_result = to_weird_case(input_word)
        expected_result = "WeIrD StRiNg"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
