import pytest
from typing import Any

from banking.domain.money import (
    Currency,
)

class TestCurrency:
    """
    Even better approach than this:
    ```python

        def test_input(self):
        with pytest.raises(TypeError):
            Currency()

        with pytest.raises(TypeError):
            Currency(1, 2)

        with pytest.raises(TypeError):
            Currency("5", "1")

        with pytest.raises(TypeError):
            Currency("USD", True)


        #  with pytest.raises(TypeError): # This one should fail
        #              ^^^^^^^^^^^^^^^^^^^^^^^^
        # E       Failed: DID NOT RAISE TypeError
        with pytest.raises(TypeError): # This one should fail,
            Currency("USD", 2)

    ```

    """
    @pytest.mark.parametrize(
        "args",
        [
            (),
            (1, 2),
            ("5", "1"),
            ("USD", True),
        ]
    )
    def test_input(self, args: tuple[Any, ...]) -> None:
        with pytest.raises(TypeError):
            Currency(*args)



