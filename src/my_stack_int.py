# ./src/my_stack_int.py

from typing import List


class MyStackInt:
    """
    A stack of integers supporting O(1) push, pop, and max operations.
    """

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        self._stack: List[int] = []
        self._max_stack: List[int] = []

    def push(self, num: int) -> None:
        """
        Pushes a number onto the top of the stack.

        Args:
            num (int): The number to be added.
        """
        self._stack.append(num)
        if not self._max_stack or num >= self._max_stack[-1]:
            self._max_stack.append(num)

    def pop(self) -> int:
        """
        Removes and returns the number from the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            int: The number removed from the top of the stack.
        """
        if not self._stack:
            raise IndexError("Stack is empty")
        val = self._stack.pop()
        if val == self._max_stack[-1]:
            self._max_stack.pop()
        return val

    def max(self) -> int:
        """
        Returns the maximum number currently in the stack.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            int: The maximum number in the stack.
        """
        if not self._max_stack:
            raise IndexError("Stack is empty")
        return self._max_stack[-1]
