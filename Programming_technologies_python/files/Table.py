from dataclasses import dataclass
from typing import List, Optional
from abc import ABC, abstractmethod
import json


class Storage(ABC):
    @abstractmethod
    def save_to_json(self, filename: str) -> None:
        pass

    @abstractmethod
    def save_to_txt(self, filename: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def load_from_file(filename: str) -> 'Table':
        pass


@dataclass
class Item:
    name: str
    cost: int


class Table(Storage):
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.items: List = []

    def add_item(self, item: Item) -> bool:
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Item '{item.name}' added to the table.")
            return True
        print("Table is full, cannot add more items.")
        return False

    def remove_item(self, item_name: str) -> bool:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Item '{item.name}' removed from the table.")
                return True
        print(f"Item '{item_name}' not found on the table.")
        return False

    def find_item_by_name(self, name: str) -> Optional[Item]:
        for item in self.items:
            if item.name == name:
                return item
        return None

    def find_item_by_cost(self, cost: int) -> List[Item]:
        found_items = []
        for item in self.items:
            if item.cost == cost:
                found_items.append(item)
        return found_items

    def total_cost(self) -> int:
        return sum(item.cost for item in self.items)

    def display(self) -> None:
        print(f"Items on the table:")
        for item in self.items:
            print(f"Name: {item.name}, Cost: {item.cost}")

    def save_to_json(self, filename: str) -> None:
        data = {"capacity": self.capacity, "items": [(item.name, item.cost) for item in self.items]}
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Table state saved to {filename}.")

    def save_to_txt(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(f"Capacity: {self.capacity}\n")
            for item in self.items:
                f.write(f"Name: {item.name}, Cost: {item.cost}\n")
        print(f"Table state saved to {filename}.")

    @staticmethod
    def load_from_file(filename: str) -> 'Table':
        with open(filename, 'r') as f:
            data = json.load(f)
        tbl = Table(data['capacity'])
        for item_data in data['items']:
            tbl.add_item(Item(item_data[0], item_data[1]))
        print(f"Table state loaded from {filename}.")
        return tbl


if __name__ == "__main__":
    item1 = Item("Fork", 5)
    item2 = Item("Knife", 8)
    item3 = Item("Plate", 10)

    table = Table(5)

    table.add_item(item1)
    table.add_item(item2)
    table.add_item(item3)

    table.display()

    table.remove_item("Fork")

    found_item = table.find_item_by_name("Knife")
    if found_item:
        print(f"Found item: {found_item.name}, Cost: {found_item.cost}")

    table.save_to_json("Table_state.json")

    loaded_table = Table.load_from_file("Table_state.json")
    loaded_table.display()
