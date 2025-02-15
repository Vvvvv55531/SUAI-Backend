from dataclasses import dataclass
from typing import List


@dataclass
class Products:
    _name: str
    _max_temp: float
    _min_temp: float

    def __str__(self) -> str:
        return f"Product({self._name}, {self._max_temp}, {self._min_temp})"

    def check_temp(self, temp: float) -> bool:
        if (temp > self._min_temp) and (temp < self._max_temp):
            return True
        return False

    def check_name(self) -> str:
        return self._name


class Fridge:
    def __init__(self, t: float):
        self._storage: List[Products] = []
        self._temperature: float = t

    def add_product(self, product: Products) -> None:
        if product.check_temp(self._temperature):
            self._storage.append(product)
        else:
            print(f"\nStorage temperature is unsuitable for {product}!")

    def del_product(self, product: Products) -> None:
        if self.is_exist(product):
            raise ValueError("Product doesn't exist")

        for i in range(len(self._storage)):
            if self._storage[i] == product:
                self._storage.remove(product)
                break

    def search_product(self, name: str) -> None:
        for i in range(len(self._storage)):
            if self._storage[i].check_name() == name:
                print("\nFound product:", self._storage[i])

    def storage_fullness(self) -> None:
        print("\nStorage fullness:", len(self._storage))

    def storage_states(self) -> None:
        print("\nStorage status:")
        for i in range(len(self._storage)):
            print(self._storage[i])

    def is_empty(self) -> bool:
        if len(self._storage) > 0:
            return False
        return True

    def is_exist(self, product: Products) -> bool:
        for i in range(len(self._storage)):
            if self._storage[i] == product:
                return False
        return True


class Freezer(Fridge):
    pass
