from typing import TypeAlias, Self

Code: TypeAlias = str

class Currency:
    def __init__(self, code: Code, exponent: int) -> None:
        """
        Initialize attributes that represent the Currency.

        :param code: every currency should have some code, e.g: UZS, USD, RUB, etc.
        :param exponent: the number of digits after the "."
        """
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


class Money:
    def __init__(self, currency: Currency, amount: int) -> None:
        self.amount = amount
        self.currency = currency

    # TODO: Implement validation for Money.
    # TODO: Implement __add__, __sub__ and the rest of dunder methods needed to perform number-like operations.
    @classmethod
    def uzs(cls, amount: int) -> Self:
        return cls(get_currency("UZS"), amount)

    @classmethod
    def usd(cls, amount: int) -> Self:
        return cls(get_currency("USD"), amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self.currency, self.amount) == (other.currency, other.amount)

    def __hash__(self) -> int:
        return hash((self.currency, self.amount))

    def __repr__(self) -> str:
        return f"Money({self.currency.code}, {self.amount})"
