"""
Passport Immitation Classes.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import Self

from _exceptions import PassportValidationFailed
from base import BaseMapping
from validators import PassportValidator

PASSPORT_ID = 1


class BasePassport(ABC):
    doc_type: str
    country_code: str

    first_name: str
    last_name: str
    date_of_birth: date
    expiry_date: date
    identifier: str

    id_: int

    def __new__(cls, *args, **kwargs) -> Self:
        global PASSPORT_ID

        new_instance = super().__new__(cls)
        new_instance.id_ = PASSPORT_ID

        PASSPORT_ID = PASSPORT_ID + 1

        return new_instance

    def is_valid(self) -> bool:
        return date.today() < self.expiry_date

    @abstractmethod
    def validate(self, passport_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def calculate_age(self) -> int:
        raise NotImplementedError


class UZBPassport(BasePassport):
    doc_type: str = "P"
    country_code: str = "UZB"

    def __init__(
        self,
        first_name: str,
        last_name: str,
        date_of_birth: date,
        expiry_date: date,
        identifier: str,
    ):
        self.first_name = first_name
        self.last_name = last_name

        self.date_of_birth = date_of_birth
        self.expiry_date = expiry_date

        self.identifier = self.validate(identifier)

    def calculate_age(self) -> int:
        today = date.today()

        birthday_has_passed = (today.month, today.day) >= (
            self.date_of_birth.month,
            self.date_of_birth.day,
        )

        return today.year - self.date_of_birth.year - (0 if birthday_has_passed else 1)

    def validate(self, passport_id: str) -> str:
        if not PassportValidator.match(passport_id):
            raise PassportValidationFailed(
                "Invalid passport format, it should have two letter and 7 digits!"
            )

        return passport_id


class PassportSet(BaseMapping[str, BasePassport]):
    entity_class = BasePassport
