import unittest
from src.challenge40 import verify_dna_sequence_validity


class TestChallenge40(unittest.TestCase):

    def test_should_return_invalid_when_dna_sequence_is_empty(self):
        dna_sequence = ""
        actual_result = verify_dna_sequence_validity(dna_sequence)

        self.assertFalse(actual_result)

    def test_should_return_valid_when_dna_sequence_contains_a_valid_nucleotide(self):
        dna_sequence = "A"
        actual_result = verify_dna_sequence_validity(dna_sequence)

        self.assertTrue(actual_result)

    def test_should_return_valid_when_dna_sequence_contains_two_valid_nucleotides(self):
        dna_sequence = "AT"
        actual_result = verify_dna_sequence_validity(dna_sequence)

        self.assertTrue(actual_result)

    def test_should_return_invalid_when_dna_sequence_contains_invalid_nucleotides_in_the_end_of_the_sequence(self):
        dna_sequence = "ATGCX"
        actual_result = verify_dna_sequence_validity(dna_sequence)

        self.assertFalse(actual_result)


if __name__ == '__main__':
    unittest.main()
