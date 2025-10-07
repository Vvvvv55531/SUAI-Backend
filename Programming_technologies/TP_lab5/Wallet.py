from typing import Dict
import json
from abc import ABC, abstractmethod


class WalletInterface(ABC):
    @abstractmethod
    def save_to_json(self, filename: str) -> None:
        pass

    @abstractmethod
    def save_to_txt(self, filename: str) -> None:
        pass

    @abstractmethod
    def load_from_json(self, filename: str) -> 'Wallet':
        pass

    @abstractmethod
    def load_from_txt(self, filename: str) -> 'Wallet':
        pass


class Wallet(WalletInterface):
    def __init__(self) -> None:
        self.money: Dict = {}

    def add_money(self, currency: str, amount: float) -> bool:
        if currency in self.money:
            self.money[currency] += amount
            return True
        self.money[currency] = amount
        return False

    def total_in_currency(self, target_currency: str, r: float) -> float:
        total: float = 0.0
        for currency, amount in self.money.items():
            total += self.convert_money(currency, target_currency, r) * amount
        return total

    def amount_in_currency(self, currency: str) -> float:
        return self.money.get(currency, 0.0)

    @staticmethod
    def convert_money(from_currency: str, to_currency: str, rate: float) -> float:
        if from_currency == to_currency:
            return 1.0
        return rate

    def save_to_json(self, filename: str) -> None:
        with open(filename, 'w') as file:
            json.dump(self.money, file)

    def save_to_txt(self, filename: str) -> None:
        with open(filename, 'w') as file:
            for currency, amount in self.money.items():
                file.write(f"{currency}: {amount}\n")

    @classmethod
    def load_from_json(cls, filename: str) -> 'Wallet':
        wlt: Wallet = Wallet()
        with open(filename, 'r') as file:
            wlt.money = json.load(file)
        return wlt

    @classmethod
    def load_from_txt(cls, filename: str) -> 'Wallet':
        w: Wallet = Wallet()
        with open(filename, 'r') as file:
            for line in file:
                currency, amount_str = line.strip().split(': ')
                w.money[currency] = float(amount_str)
        return w


if __name__ == "__main__":
    wallet = Wallet()

    wallet.add_money("RUB", 10000.0)
    wallet.add_money("USD", 500.0)
    wallet.add_money("EUR", 300.0)

    print("Total in RUB:", wallet.total_in_currency("RUB", 1.0))
    print("Total in USD:", wallet.total_in_currency("USD", 9.0))
    print("Total in EUR:", wallet.total_in_currency("EUR", 11.0))

    print("Amount of USD:", wallet.amount_in_currency("USD"))

    wallet.convert_money("EUR", "USD", 11.0)

    wallet.save_to_json("Wallet.json")

    loaded_wallet = Wallet.load_from_json("Wallet.json")
    print("Loaded Wallet:", loaded_wallet.money)
