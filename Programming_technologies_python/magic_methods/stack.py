from typing import List, TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, size: int) -> None:
        self._stack: List[T] = []
        self._len: int = 0
        self._max_len: int = size

    def __str__(self) -> str:
        return f"Stack: {self._stack}"

    def __len__(self) -> int:
        return self._len

    def __call__(self, el: T) -> bool:
        if self._is_full():
            raise ValueError("Stack is full")

        self._stack.append(el)
        self._len += 1
        return True

    def __delitem__(self, index: int) -> bool:
        if index != -1:
            raise ValueError("Only the last element [-1] can be removed from the stack")

        if self._is_empty():
            raise ValueError("Stack is empty")

        del self._stack[index]
        self._len -= 1
        return True

    def _is_full(self) -> bool:
        if self._len >= self._max_len:
            return True
        return False

    def _is_empty(self) -> bool:
        if self._len == 0:
            return True
        return False
