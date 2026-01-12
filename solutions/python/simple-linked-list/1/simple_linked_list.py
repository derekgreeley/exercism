# simple_linked_list.py

from __future__ import annotations
from typing import Iterable, Iterator, Optional, Any


class EmptyListException(Exception):
    """Exception raised when the linked list is empty."""

    def __init__(self, message: str):
        super().__init__(message)


class _Node:
    __slots__ = ("_value", "_next")

    def __init__(self, value: Any, next_node: Optional["_Node"] = None):
        self._value = value
        self._next = next_node

    def value(self) -> Any:
        return self._value

    def next(self) -> Optional["_Node"]:
        return self._next


class LinkedList:
    def __init__(self, values: Optional[Iterable[Any]] = None):
        self._head: Optional[_Node] = None
        self._len = 0

        if values is not None:
            # For this exercise, constructing from an iterable should result in the
            # LAST item becoming the head (stack-like behavior).
            for v in values:
                self.push(v)

    def __len__(self) -> int:
        return self._len

    def head(self) -> _Node:
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: Any) -> None:
        self._head = _Node(value, self._head)
        self._len += 1

    def pop(self) -> Any:
        if self._head is None:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = node.next()
        self._len -= 1
        return node.value()

    def __iter__(self) -> Iterator[Any]:
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next()

    def reversed(self) -> "LinkedList":
        # Return a NEW LinkedList whose iteration yields items in reverse order
        # of the current list's iteration.
        rev = LinkedList()
        current = self._head
        while current is not None:
            rev.push(current.value())
            current = current.next()
        return rev
