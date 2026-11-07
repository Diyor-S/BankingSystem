from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

from .cli import Cli
from .web import Web


if TYPE_CHECKING:
    from _banking.app import App


class UserInterfaceAdapter(Protocol):
    app: App

    def run(self) -> None: ...
    def startup(self) -> None: ...
    def exit(self) -> None: ...


__all__ = [
    "Cli",
    "Web",
]