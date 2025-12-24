# ./tests/test_number_box.py

import unittest
from src.number_box import NumberBox
from typing import Callable


class TestNumberBox(unittest.TestCase):
    """
    Concrete test suite for the `NumberBox` class.

    Tests all public methods including:
        - add_number
        - remove_number
        - remove_numbers_predicate
        - remove_numbers_range
        - distinct
        - iteration
    """

    def setUp(self):
        """
        Initialize a fresh NumberBox before each test.
        """
        self.nb = NumberBox()

    def test_add_number_and_iteration(self):
        """
        Test adding numbers and iterating in sorted order.
        """
        test_data = [5, 1, 3, 2, 5, 4, 3]
        for num in test_data:
            print(f"Adding number {num} to NumberBox")
            self.nb.add_number(num)

        expected = [1, 2, 3, 3, 4, 5, 5]
        print(f"Expecting sorted numbers: {expected}")
        self.assertEqual(list(self.nb), expected)

    def test_remove_number(self):
        """
        Test removing numbers, including missing elements.
        """
        for num in [1, 2, 3, 4, 5]:
            self.nb.add_number(num)

        test_data = [
            (3, 3),   # number exists
            (10, None),  # number does not exist
        ]
        for num, expected in test_data:
            print(f"Removing number {num}, expecting return {expected}")
            with self.subTest(num=num):
                self.assertEqual(self.nb.remove_number(num), expected)

    def test_remove_numbers_predicate(self):
        """
        Test removing numbers by predicate.
        """
        for num in [1, 2, 3, 4, 5]:
            self.nb.add_number(num)

        pred: Callable = lambda x: x % 2 == 0  # remove even numbers
        expected_removed_count = 2
        print(
            f"Removing numbers matching predicate, "
            f"expecting {expected_removed_count} removed"
        )
        self.assertEqual(
            self.nb.remove_numbers_predicate(pred),
            expected_removed_count
        )
        self.assertEqual(list(self.nb), [1, 3, 5])

    def test_remove_numbers_range(self):
        """
        Test removing numbers by inclusive range.
        """
        for num in [1, 2, 3, 4, 5]:
            self.nb.add_number(num)

        test_data = [
            (2, 4, 3, [1, 5]),      # remove 2,3,4
            (6, 10, 0, [1, 5]),     # remove nothing
        ]
        for min_val, max_val, expected_count, expected_list in test_data:
            print(
                f"Removing numbers in range [{min_val}, {max_val}], "
                f"expecting {expected_count} removed"
            )
            with self.subTest(min_val=min_val, max_val=max_val):
                self.assertEqual(
                    self.nb.remove_numbers_range(min_val, max_val),
                    expected_count
                )
                self.assertEqual(list(self.nb), expected_list)

    def test_distinct(self):
        """
        Test removing duplicates and leaving only unique numbers.
        """
        for num in [1, 2, 2, 3, 3, 3]:
            self.nb.add_number(num)

        expected_removed_count = 3  # remove extra 2s and 3s
        print(
            f"Removing duplicates, expecting "
            f"{expected_removed_count} removed"
        )
        self.assertEqual(self.nb.distinct(), expected_removed_count)
        self.assertEqual(list(self.nb), [1, 2, 3])


if __name__ == "__main__":
    print("Running NumberBox tests...")
    unittest.main()
