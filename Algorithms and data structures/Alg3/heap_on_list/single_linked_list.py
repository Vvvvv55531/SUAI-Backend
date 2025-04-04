from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


@dataclass
class Car:
    stamp: str
    vin: str
    engine_capacity: float
    cost: int
    average_speed: int

    def __str__(self) -> str:
        return f"Car({self.stamp}, {self.vin}, {self.engine_capacity}, {self.cost}, {self.average_speed})"


@dataclass
class SingleNode(Generic[T]):
    data: T
    next_ptr: Optional['SingleNode[T]'] = None


class SingleLinkedList(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._head: Optional[SingleNode[T]] = None
        self._tail: Optional[SingleNode[T]] = None

    def get_size(self) -> int:
        return self._length

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def is_empty(self) -> bool:
        return self._length == 0

    def push_tail(self, data: T) -> None:
        node = SingleNode[T](data, None)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        self._tail.next_ptr = node
        self._tail = node
        self._length += 1

    def push_head(self, data: T) -> None:
        node = SingleNode[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        node.next_ptr = self._head
        self._head = node
        self._length += 1

    def insert(self, index: int, data: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        if index == 0:
            self.push_head(data)
            return
        elif index == self._length - 1:
            self.push_tail(data)
            return

        node = self._head
        for i in range(0, index - 1):
            node = node.next_ptr

        insert_node = SingleNode[T](data)
        insert_node.next_ptr = node.next_ptr
        node.next_ptr = insert_node
        self._length += 1

    def get(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        node = self._head
        for i in range(0, index):
            node = node.next_ptr
        return node.data

    def remove(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        if index == 0:
            node = self._head
            self._head = node.next_ptr
            del node
            self._length -= 1
            return True

        node = self._head
        for i in range(0, index - 1):
            node = node.next_ptr

        if index == self._length - 1:
            self._tail = node
            del node.next_ptr
            node.next_ptr = None
            self._length -= 1
            return True

        delete_node = node.next_ptr
        node.next_ptr = delete_node.next_ptr
        self._length -= 1
        return True

    def for_each(self, func: Callable[[T], None]):
        node = self._head
        func(node.data)
        while node.next_ptr is not None:
            node = node.next_ptr
            func(node.data)

    def __str__(self) -> str:
        my_str: str = ""
        node = self._head
        while node is not None:
            my_str += str(node.data) + " "
            node = node.next_ptr
        return f"Current state: [{my_str}]"
