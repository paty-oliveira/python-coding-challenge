import unittest
from src.challenge47 import open_or_senior


class TestChallenge47(unittest.TestCase):
    def test_should_classify_members_as_senior_or_open(self):
        self.assertEqual(
            open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]),
            ["Open", "Open", "Senior", "Open", "Open", "Senior"],
        )
