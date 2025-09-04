import unittest
from src.challenge50 import order


class TestChallenge50(unittest.TestCase):
    def should_order_string_with_digits(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

        self.assertEqual(order(""), "")
