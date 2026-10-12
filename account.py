"""
Bank Account classes.
"""

import contextlib
from enum import StrEnum
from abc import ABC, abstractmethod
from typing import Self, Callable, Generator

from base import BaseMapping
from validators import require_password
from constants import ACCOUNT_SECRET

from _exceptions import (
    TransactionError,
    NoSuchTransactionMethod,

    DepositDeclined,
    WithdrawDeclined,
    NotEnoughMoneyToWithdraw
)

_ACCOUNT_ID = 1

class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class BaseAccount(ABC):
    id_: int

    def __new__(cls) -> Self:
        global _ACCOUNT_ID

        new_instance = super().__new__(cls)
        setattr(new_instance, "id_", _ACCOUNT_ID)

        _ACCOUNT_ID = _ACCOUNT_ID + 1

        return new_instance

    @property
    @abstractmethod
    def balance(self) -> int:
        raise NotImplementedError

    @balance.setter
    @abstractmethod
    def balance(self, value: int) -> None:
        raise NotImplementedError

    
    @contextlib.contextmanager
    def transaction(self, ts_type: TransactionType) -> Generator[Callable | None, None, None]:
        method = getattr(self, ts_type, None)

        if method is None:
            raise NoSuchTransactionMethod(
                f"Provided operation '{ts_type}' is not supported!"
            )

        initial_balance = self.balance
        
        try: 
            yield method
        except Exception as e:
            self.balance = initial_balance
            raise TransactionError(f"Transaction failed and was rolled back due to: {e}") from e


    @abstractmethod
    def deposit(self, amount: int) -> None:
        raise NotImplementedError

    
    @abstractmethod
    def withdraw(self, amount: int) -> None:
        raise NotImplementedError


class UZBAccount(BaseAccount):
    def __init__(self, balance: int = 0):
        self.balance = balance

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Type is wrong, should be 'int'")

        if value < 0:
            raise ValueError("Negative values are not permitted!")

        self._balance = value

    @require_password(ACCOUNT_SECRET)
    def deposit(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise DepositDeclined("Please, ensure that the amount is positive and integer!")

        self.balance += amount

    @require_password(ACCOUNT_SECRET)
    def withdraw(self, amount: int):
        if not isinstance(amount, int) or amount < 0:
            raise WithdrawDeclined("Please, ensure that the amount is positive and integer!")

        if self.balance < amount: 
            raise NotEnoughMoneyToWithdraw("Operation declined, not enough money on account!")

        self.balance -= amount

class AccountSet(BaseMapping[int, BaseAccount]):
    entity_class = BaseAccount

    def deposit(self, account_id: int, amount: int) -> None:
        account = self.find_by_id(account_id)

        if account is None:
            print(f"No account with id: {account_id!r} was found!")
            return
        else:
            account.deposit(amount)

    def withdraw(self, account_id: int, amount: int) -> None:
        account = self.find_by_id(account_id)

        if account is None:
            print(f"No account with id: {account_id!r} was found!")
            return
        else:
            account.withdraw(amount)