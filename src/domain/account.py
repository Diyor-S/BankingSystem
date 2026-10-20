import itertools
from domain.money import Money, get_currency

class BaseAccount:
    _ids = itertools.count(1)

    def __init__(self, balance: Money | None = None) -> None:
        self.id = next(self._ids)

        if balance is not None:
            if not isinstance(balance, Money):
                raise TypeError("Balance should be of type 'Money'")

            if balance.amount < 0:
                raise ValueError("Balance can not be negative")

        self._balance = balance if balance is not None else Money(get_currency("UZS"), 0)

    @property
    def balance(self) -> Money:
        return self._balance
