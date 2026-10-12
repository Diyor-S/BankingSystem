"""
Person -> Client classes.
"""

from base import BaseMapping

from passport import BasePassport
from account import BaseAccount

from constants import PASSPORT_SECRET
from validators import require_password

class Person:
    def __init__(
        self, 
        passport: BasePassport,
    ):
        self.__passport = passport

    @property
    def id_(self) -> str:
        return self.__passport.identifier

    @property
    def first_name(self) -> str:
        return self.__passport.first_name

    @property
    def last_name(self) -> str:
        return self.__passport.last_name

    @property
    def fullname(self) -> str:
        return f"{self.__passport.first_name} {self.__passport.last_name}"

    @property
    def age(self) -> int:
        return self.__passport.calculate_age()

    @property
    @require_password(PASSPORT_SECRET)
    def passport(self) -> str:
        return self.__passport.identifier

    @property
    def is_expired(self) -> bool:
        return not self.__passport.is_valid()


class Client(Person):
    def __init__(
        self,
        passport: BasePassport,
        account: BaseAccount,
    ):
        super().__init__(passport)

        self.__account = account

    @property
    def account(self) -> BaseAccount:
        return self.__account

    @property
    def balance(self) -> int:
        return self.__account.balance

class ClientSet(BaseMapping[int, Client]):
    entity_class = Client

    