import itertools
from domain.money import Money, get_currency

class NotEnoughMoneyInBalance(Exception): ...

class BaseAccount:
    _ids = itertools.count(1)

    def __init__(self, balance: Money | None = None) -> None:
        self.id = next(self._ids)

        if balance is not None:
            self._check_balance(balance)

            self._balance = balance
        else:
            self._balance =  Money(get_currency("UZS"), 0)

    @property
    def balance(self) -> int:
        return self._balance.amount

    @property
    def currency(self) -> str:
        return self._balance.currency.code

    @staticmethod
    def _check_balance(balance: Money) -> None:
        if balance is not None:
            if not isinstance(balance, Money):
                raise TypeError("Balance should be of type 'Money'")

    def deposit(self, balance_to_add: Money) -> None:
        self._check_balance(balance_to_add)

        self._balance += balance_to_add

    def withdraw(self, balance_to_withdraw: Money) -> None:
        self._check_balance(balance_to_withdraw)

        if self._balance < balance_to_withdraw:
            raise NotEnoughMoneyInBalance("Not enough money in balance")

        self._balance -= balance_to_withdraw
