import unittest
from src.challenge52 import break_camel_case


class TestChallenge52(unittest.TestCase):
    def should_break_camel_case(self):
        self.assertEqual(break_camel_case("helloWorld"), "hello World")
        self.assertEqual(break_camel_case("camelCase"), "camel Case")
        self.assertEqual(break_camel_case("breakCamelCase"), "break Camel Case")
        self.assertEqual(break_camel_case("", ""))
