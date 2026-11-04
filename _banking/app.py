"""
Application implementation for Banking System.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from config import get_settings

if TYPE_CHECKING:
    from config import Settings


class App:
    """
    Main class that is an entrypoint to the application.
    """

    def __init__(self) -> None:
        self._settings = get_settings()
        # self._interface = get_interface()

    @property
    def settings(self) -> Settings:
        return self._settings

    @property
    def interface(self):
        return self.settings.interface

    def run(self) -> None:
        print("Application running...")

        print("User Interface %r is loaded." % self.settings.interface.type)
