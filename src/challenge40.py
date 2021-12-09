"""
    Implement a function that return if a DNA sequence is valid.
    Input:
        - DNA sequence - String

    >> verify_dna_sequence_validity("ATGC")
    >> True

    >> verify_dna_sequence_validity("ATXG")
    >> False
"""


def verify_dna_sequence_validity(sequence):
    alphabet = ["A", "T", "G", "C"]

    if len(sequence) == 0:
        return False
    else:
        for base in sequence:
            if base not in alphabet:
                return False
    return True
