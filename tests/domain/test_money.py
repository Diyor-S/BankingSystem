import pytest
from typing import Any

from banking.domain.money import Currency, Money

class TestMoneyflow:
    @pytest.mark.parametrize(
        "args",
        [
            (),
            ("UZS", 10),
            (Currency("USD", 2), "100"),
            (Currency("USD", 2), True)
        ]
    )
    def test_input(self, args: tuple[Any, ...]) -> None:
        with pytest.raises(TypeError):
            Money(args)

        with pytest.raises(ValueError):
            Money(Currency("USD", 2), -100)


        currency = Currency("UZS", 2)
        Money(currency, 1000)

    def test_eq(self) -> None:
        pass

    def test_transfers(self) -> None:
        pass