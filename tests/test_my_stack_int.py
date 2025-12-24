# tests/test_my_stack_int.py

import unittest
from src import MyStackInt


class TestMyStackInt(unittest.TestCase):
    """Unit tests for MyStackInt class."""

    def test_stack_operations(self):
        """Test push, pop, and max for various scenarios."""
        s = MyStackInt()
        test_data = [
            ("push", 3, None, None),
            ("push", 5, None, None),
            ("max", None, 5, None),
            ("pop", None, 5, None),
            ("max", None, 3, None),
            ("pop", None, 3, None),
        ]

        for op, val, expected, _ in test_data:
            with self.subTest(op=op, val=val):
                if op == "push":
                    s.push(val)
                elif op == "pop":
                    self.assertEqual(s.pop(), expected)
                elif op == "max":
                    self.assertEqual(s.max(), expected)

    def test_empty_pop_max(self):
        """Test that pop and max raise IndexError on empty stack."""
        s = MyStackInt()
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.max()


if __name__ == "__main__":
    unittest.main()
