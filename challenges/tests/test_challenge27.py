import unittest
from src.challenge27 import obtain_high_scoring_word


class TestChallenge27(unittest.TestCase):

    def test_should_return_the_score_of_one_word(self):
        input_phrase = "ab"
        actual_result = obtain_high_scoring_word(input_phrase)
        expected_result = "ab"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_highest_scoring_word_between_two_words(self):
        input_phrase = "ab cd"
        actual_result = obtain_high_scoring_word(input_phrase)
        expected_result = "cd"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_highest_scoring_word_between_two_three_words(self):
        input_phrase = "ab xp ru"
        actual_result = obtain_high_scoring_word(input_phrase)
        expected_result = "xp"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_word_that_appears_first_when_two_words_have_the_same_score(self):
        input_phrase = "aaaa bb"
        actual_result = obtain_high_scoring_word(input_phrase)
        expected_result = "aaaa"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
