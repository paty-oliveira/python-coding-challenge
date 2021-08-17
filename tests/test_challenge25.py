import unittest
from src.challenge25 import likes


class TestChallenge25(unittest.TestCase):

    def test_should_return_no_likes_when_names_list_is_empty(self):
        input_names = []
        actual_result = likes(input_names)
        expected_result = "no one likes this"

        self.assertEqual(actual_result, expected_result)

    def test_should_return_one_name_who_likes_the_post(self):
        input_names = ["Peter"]
        actual_result = likes(input_names)
        expected_result = "Peter likes this"

        self.assertEqual(actual_result, expected_result)

    def test_should_return_two_names_who_like_the_post(self):
        input_names = ["Jacob", "Alex"]
        actual_result = likes(input_names)
        expected_result = "Jacob and Alex like this"

        self.assertEqual(actual_result, expected_result)

    def test_should_return_three_names_who_like_the_post(self):
        input_names = ["Max", "John", "Mark"]
        actual_result = likes(input_names)
        expected_result = "Max, John and Mark like this"

        self.assertEqual(actual_result, expected_result)

    def test_should_return_four_names_who_like_the_post(self):
        input_names = ["Alex", "Jacob", "Mark", "Max"]
        actual_result = likes(input_names)
        expected_result = "Alex, Jacob and 2 others like this"

        self.assertEqual(actual_result, expected_result)

    def test_should_return_five_names_who_like_the_post(self):
        input_names = ["Alex", "Jacob", "Mark", "Max", "Patricia"]
        actual_result = likes(input_names)
        expected_result = "Alex, Jacob and 3 others like this"

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
