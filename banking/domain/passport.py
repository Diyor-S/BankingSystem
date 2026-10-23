import itertools
from datetime import date
from typing import Sequence

from core.validators import PassportValidator
from core.exceptions import PassportValidationFailed


class BasePassport:
    _ids: itertools.count  = itertools.count(1)

    def __init__(self, first_name: str, last_name: str, *, identity: str, birth_date: date, expires_at: date) -> None:
        self.id = next(self._ids)

        self._check_str_names([first_name, last_name])

        if not PassportValidator.fullmatch(identity):
            raise PassportValidationFailed(
                "Does not match the passport protocol.\n"
                "Expected 2 English letters followed by 7 digits (e.g., AB1234567)."
            )

        if birth_date > date.today():
            raise ValueError("How can birth_date be later than today?")

        if expires_at < date.today():
            raise ValueError("How can the expire date be before today?")

        self.first_name = first_name
        self.last_name = last_name
        self._identity = identity
        self.birth_date = birth_date
        self.expires_at = expires_at

    @property
    def identity(self) -> str:
        return self._identity

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_expired(self) -> bool:
        return self.expires_at < date.today()

    @staticmethod
    def _check_str_names(fields: Sequence[str]) -> None:
        for field in fields:
            if not isinstance(field, str):
                raise TypeError("Should be of type 'str'")

            if len(field) < 1:
                raise ValueError(f"At least 1 character should be present! But got {len(field)}")





