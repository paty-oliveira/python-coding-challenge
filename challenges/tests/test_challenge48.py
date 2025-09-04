import unittest
from src.challenge48 import to_camel_case


class TestChallenge48(unittest.TestCase):
    def should_convert_text_to_camel_case(self):
        self.assertEqual(to_camel_case("the-stealth-warrior"), "theStealthWarrior")
        self.assertEqual(to_camel_case("The_Stealth_Warrior"), "TheStealthWarrior")
        self.assertEqual(to_camel_case("The_Stealth-Warrior"), "TheStealthWarrior")
