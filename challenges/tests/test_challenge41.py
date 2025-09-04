import unittest
from src.challenge41 import generate_hashtag


class TestChallenge41(unittest.TestCase):

    def test_should_return_empty_hashtag_when_the_input_phrase_is_empty(self):
        phrase = ""
        actual_result = generate_hashtag(phrase)
        expected_result = ""

        self.assertEqual(expected_result, actual_result)

    def test_should_return_a_hashtag_of_an_input_phrase_with_one_word(self):
        phrase = "hello"
        actual_result = generate_hashtag(phrase)
        expected_result = "#Hello"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_a_hashtag_of_an_input_phrase_with_two_words(self):
        phrase = "hello world"
        actual_result = generate_hashtag(phrase)
        expected_result = "#HelloWorld"

        self.assertEqual(expected_result, actual_result)

    def test_should_return_a_hashtag_of_an_input_phrase_with_many_words(self):
        phrase = " hello world thanks for trying my Kata "
        actual_result = generate_hashtag(phrase)
        expected_result = "#HelloWorldThanksForTryingMyKata"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
