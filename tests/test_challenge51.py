import unittest
from src.challenge51 import increment_string


class TestChallenge51(unittest.TestCase):
    def should_increment_string(self):
        self.assertEqual(increment_string("foo"), "foo1")

        self.assertEqual(increment_string("foobar001"), "foobar002")

        self.assertEqual(increment_string("foobar1"), "foobar2")

        self.assertEqual(increment_string("foobar00"), "foobar01")

        self.assertEqual(increment_string("foobar99", "foobar100"))

        self.assertEqual(increment_string("fo99obar99", "fo99obar100"))

        self.assertEqual(increment_string(""), "1")
