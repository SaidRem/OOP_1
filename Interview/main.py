from typing import Any, List


class Stack:
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self._items: List[Any] = []

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack.

        Args:
            item (Any): The item to be added.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.

        Returns:
            Any: The item from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item from the stack without removing it.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            IndexError: if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self._items)
