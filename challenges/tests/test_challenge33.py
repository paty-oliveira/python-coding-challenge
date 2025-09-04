import unittest
from src.challenge33 import extract_stock


class TestChallenge33(unittest.TestCase):

    def test_should_return_the_stock_list_of_one_book(self):
        book_categories = ["A"]
        book_stock = ["ABART 20"]
        actual_result = extract_stock(book_categories, book_stock)
        expected_result = [("A", 20)]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_stock_list_of_two_book_of_the_same_category(self):
        book_categories = ["A"]
        book_stock = ["ABART 20", "ABATT 10"]
        actual_result = extract_stock(book_categories, book_stock)
        expected_result = [("A", 30)]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_stock_list_of_three_different_book_categories(self):
        book_categories = ["A", "B", "C"]
        book_stock = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89"]
        actual_result = extract_stock(book_categories, book_stock)
        expected_result = [("A", 20), ("B", 114), ("C", 50)]

        self.assertEqual(expected_result, actual_result)

    def test_should_return_the_stock_list_when_stock_has_categories_book_not_present_in_categories_list(self):
        book_categories = ["A", "B", "C"]
        book_stock = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        actual_result = extract_stock(book_categories, book_stock)
        expected_result = [("A", 20), ("B", 114), ("C", 50)]

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
