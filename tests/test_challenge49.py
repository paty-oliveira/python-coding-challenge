import unittest
from src.challenge49 import extract_file_name


class TestChallenge49(unittest.TestCase):
    def should_extract_file_name(self):
        self.assertEqual(
            extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"),
            "FILE_NAME.EXTENSION",
        )
        self.assertEqual(
            extract_file_name(
                "1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34",
                "FILE_NAME.EXTENSION",
            )
        )
