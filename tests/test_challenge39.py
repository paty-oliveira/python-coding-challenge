import unittest
from src.challenge39 import first_non_repeating_letter


class TestChallenge39(unittest.TestCase):

    def test_should_return_itself_letter_when_the_word_has_one_letter(self):
        word = "T"
        actual_result = first_non_repeating_letter(word)
        expected_result = "T"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_first_letter_when_the_word_has_two_letters(self):
        word = "te"
        actual_result = first_non_repeating_letter(word)
        expected_result = "t"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_first_letter_that_is_not_repeated_anywhere(self):
        word = "Tet"
        actual_result = first_non_repeating_letter(word)
        expected_result = "e"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_empty_string_when_word_contains_all_repeating_letters(self):
        word = "TTttttTTT"
        actual_result = first_non_repeating_letter(word)
        expected_result = ""

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
