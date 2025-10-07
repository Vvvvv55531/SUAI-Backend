from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    _name: str
    _type: str
    _cost: float
    _weight: float

    def __str__(self) -> str:
        return f"Product({self._name}, {self._type}, {self._cost}, {self._weight})"

    def get_type(self) -> str:
        return self._type

    def get_cost(self) -> float:
        return self._cost

    def get_weight(self) -> float:
        return self._weight


class Scales:
    def __init__(self, w: float):
        self._storage: List[Product] = []
        self._current_weight: float = 0.0
        self._max_weight: float = w

    def add_product(self, product: Product) -> None:
        if (self._current_weight + product.get_weight()) <= self._max_weight:
            self._storage.append(product)
            self._current_weight += product.get_weight()
        else:
            print(f"\nStorage weight is unsuitable for {product}!")

    def del_product(self, product: Product) -> None:
        if self.is_exist(product):
            raise ValueError("Product doesn't exist")

        for i in range(len(self._storage)):
            if self._storage[i] == product:
                self._storage.remove(product)
                self._current_weight -= product.get_weight()
                break

    def storage_states(self) -> None:
        print("\nStorage status:")
        for i in range(len(self._storage)):
            print(self._storage[i])

    def current_weight(self) -> None:
        print("\nCurrent weight:", self._current_weight)

    def sort_by_cost(self) -> None:
        for i in range(0, len(self._storage)):
            current_min = self._storage[i].get_cost()
            min_index = i
            for j in range(i, len(self._storage)):
                if self._storage[j].get_cost() < current_min:
                    current_min = self._storage[j].get_cost()
                    min_index = j
            self._swap(i, min_index)

    def sort_by_weight(self) -> None:
        for i in range(0, len(self._storage)):
            current_min = self._storage[i].get_weight()
            min_index = i
            for j in range(i, len(self._storage)):
                if self._storage[j].get_weight() < current_min:
                    current_min = self._storage[j].get_weight()
                    min_index = j
            self._swap(i, min_index)

    def _swap(self, index_1: int, index_2: int) -> None:
        value: Product = self._storage[index_1]
        self._storage[index_1] = self._storage[index_2]
        self._storage[index_2] = value

    def min_cost(self) -> None:
        if self.is_empty():
            raise ValueError("Storage is empty")

        min_value: Product = min(self._storage, key=lambda x: x.get_cost())
        print("\nMinimum cost:", min_value)

    def max_weight(self) -> None:
        if self.is_empty():
            raise ValueError("Storage is empty")

        max_value: Product = max(self._storage, key=lambda x: x.get_weight())
        print("\nMaximum weight:", max_value)

    def is_empty(self) -> bool:
        if self._current_weight > 0.0:
            return False
        return True

    def is_exist(self, product: Product) -> bool:
        for i in range(len(self._storage)):
            if self._storage[i] == product:
                return False
        return True

    def weight_of_type(self, product_type: str) -> None:
        weight_value: float = 0.0
        for i in range(len(self._storage)):
            if self._storage[i].get_type() == product_type:
                weight_value += self._storage[i].get_weight()
        print("\nCurrent weight of type:", weight_value)
