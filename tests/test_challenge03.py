import unittest
from src.challenge03 import online_count


class TestChallenge03(unittest.TestCase):
    def test_should_return_zero_when_status_is_empty(self):
        input_param = {}
        expected_result = 0
        current_result = online_count(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_one_online_person(self):
        input_param = {"Alice": "online"}
        expected_result = 1
        current_result = online_count(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_zero_online_persom(self):
        input_param = {"Alice": "offline",
                       "Bob": "offline",
                       "Eve": "offline"
                       }
        expected_result = 0
        current_result = online_count(input_param)

        self.assertEqual(current_result, expected_result)

    def test_should_return_two_online_person(self):
        input_param = {"Alice": "offline",
                       "Bob": "offline",
                       "Eve": "offline",
                       "Maria": "online",
                       "Tiago": "online"
                       }
        expected_result = 2
        current_result = online_count(input_param)

        self.assertEqual(current_result, expected_result)




if __name__ == '__main__':
    unittest.main()
