import unittest
from src.challenge42 import top_three_words


class TestChallenge42(unittest.TestCase):

    def test_should_return_empty_list_when_text_is_empty(self):
        text = ""
        actual_result = top_three_words(text)
        expected_result = []

        self.assertEqual(expected_result, actual_result)

    def test_should_return_frequency_of_three_words(self):
        text = "hi hi test"
        actual_result = top_three_words(text)
        expected_result = ["hi", "test"]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_frequency_of_many_words(self):
        text = "e e e e DDD ddd DdD ddd ddd aa aA Aa bb cc cC e e e"
        actual_result = top_three_words(text)
        expected_result = ["e", "ddd", "aa"]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_three_most_frequent_words_in_the_text(self):
        text = "In a Village of Kings, there are a beautiful leaf. This leaf contains a color red. Kings exists."
        actual_result = top_three_words(text)
        expected_result = ["a", "kings", "leaf"]

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
