# ./src/number_box.py

from sortedcontainers import SortedList
from typing import Callable, Iterator, Optional


class NumberBox:
    """
    A container for integers that maintains sorted order
    and provides methods for adding, removing, and filtering numbers.
    """

    def __init__(self) -> None:
        """
        Initializes an empty NumberBox.
        """
        self._numbers: SortedList = SortedList()

    def __iter__(self) -> Iterator[int]:
        """
        Returns an iterator over the numbers in ascending order.

        Returns:
            Iterator[int]: Iterator of numbers.
        """
        return iter(self._numbers)

    def add_number(self, num: int) -> None:
        """
        Adds a number to the box in sorted order.

        Args:
            num (int): Number to add.
        """
        self._numbers.add(num)

    def remove_number(self, num: int) -> Optional[int]:
        """
        Removes a number from the box if it exists.

        Args:
            num (int): Number to remove.

        Returns:
            Optional[int]: The removed number if present, otherwise None.
        """
        res = None
        try:
            self._numbers.remove(num)
            res = num
        except ValueError:
            pass
        return res

    def remove_numbers_predicate(self, pred: Callable[[int], bool]) -> int:
        """
        Removes all numbers satisfying a predicate.

        Args:
            pred (Callable[[int], bool]): A function that returns True for
                                          numbers to remove.

        Returns:
            int: Count of removed numbers.
        """
        removed_count = 0
        new_list = SortedList()
        for num in self._numbers:
            if pred(num):
                removed_count += 1
            else:
                new_list.add(num)
        self._numbers = new_list
        return removed_count

    def remove_numbers_range(self, min_value: int, max_value: int) -> int:
        """
        Removes all numbers within a given inclusive range.

        Args:
            min_value (int): Minimum value of the range.
            max_value (int): Maximum value of the range.

        Returns:
            int: Count of removed numbers.
        """
        left = self._numbers.bisect_left(min_value)
        right = self._numbers.bisect_right(max_value)
        removed_count = right - left
        del self._numbers[left:right]
        return removed_count

    def distinct(self) -> int:
        """
        Removes duplicate numbers, leaving only distinct elements.

        Returns:
            int: Count of removed duplicates.
        """
        removed_count = 0
        if self._numbers:
            new_list = SortedList()
            last_num: Optional[int] = None

            for num in self._numbers:
                if num == last_num:
                    removed_count += 1
                else:
                    new_list.add(num)
                    last_num = num

            self._numbers = new_list
        return removed_count
