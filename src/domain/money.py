from __future__ import annotations

from functools import total_ordering
from typing import TypeAlias, Self

Code: TypeAlias = str

class Currency:
    def __init__(self, code: Code, exponent: int) -> None:
        """
        Initialize attributes that represent the Currency.

        :param code: every currency should have some code, e.g: UZS, USD, RUB, etc.
        :param exponent: the number of digits after the "."
        """
        if not isinstance(code, Code):
            raise TypeError(f"Code must be of type {Code!r}, but got {type(code)!r} instead.")

        if isinstance(exponent, bool) or not isinstance(exponent, int):
            raise TypeError(f"Exponent should be of type 'int', but got {type(exponent)!r} instead")

        if exponent < 0:
            raise ValueError("Exponent must be non-negative.")

        self.code = code
        self.exponent = exponent

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Currency):
            return NotImplemented
        return (self.code, self.exponent) == (other.code, other.exponent)

    def __hash__(self) -> int:
        return hash((self.code, self.exponent))

    def __repr__(self) -> str:
        return f"Currency(code={self.code}, exponent={self.exponent})"


_CURRENCIES: dict[Code, Currency] = {
    c.code: c for c in (Currency("UZS", 2), Currency("USD", 2))
}

class CurrencyNotSupported(Exception): ...

def get_currency(code: Code) -> Currency:
    try:
        return _CURRENCIES[code]
    except KeyError:
        raise CurrencyNotSupported(f"No support for currencies with code {code!r}") from None

class IncompatibleCurrencies(Exception): ...

@total_ordering
class Money:
    def __init__(self, currency: Currency, amount: int) -> None:
        if not isinstance(currency, Currency):
            raise TypeError(f"Expected type 'Currency', but got {currency}")

        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Amount is of wrong type, should be of type 'int'")

        if amount < 0:
            raise ValueError("Amount should not be negative.")

        self._amount = amount
        self._currency = currency

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> Currency:
        return self._currency

    @classmethod
    def uzs(cls, amount: int) -> Self:
        return cls(get_currency("UZS"), amount)

    @classmethod
    def usd(cls, amount: int) -> Self:
        return cls(get_currency("USD"), amount)

    def _require_same_currency(self, other: Money) -> None:
        if self._currency != other._currency:
            raise IncompatibleCurrencies(
                f"Currencies should be of the same type!\n"
                f"Currency: {self._currency.code} is not compatible with {other._currency.code}"
            )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self._currency, self._amount) == (other._currency, other._amount)

    def __hash__(self) -> int:
        return hash((self._currency, self._amount))

    def __repr__(self) -> str:
        return f"Money({self._currency.code}, {self._amount})"

    # Number-like operations

    def __add__(self, other: object) -> Money:
        if not isinstance(other, Money):
            return NotImplemented

        self._require_same_currency(other)
        return Money(self._currency, self._amount + other._amount)

    def __sub__(self, other: object) -> Money:
        if not isinstance(other, Money):
            return NotImplemented

        self._require_same_currency(other)

        if self._amount < other._amount:
            raise ValueError("The amount would result in corrupted 'negative' state")
        return Money(self._currency, self._amount - other._amount)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented

        self._require_same_currency(other)
        return self._amount < other._amount
