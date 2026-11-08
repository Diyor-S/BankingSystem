"""
Application implementation for Banking System.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from _banking.config import get_settings
from _banking.services import ClientService

if TYPE_CHECKING:
    from _banking.config import Settings


class App:
    """
    Main class that is an entrypoint to the application.
    """

    def __init__(
        self,
        settings: Settings | None = None,
        client_service: ClientService | None = None,
    ) -> None:
        self._settings = settings or get_settings()

        # TODO: Remove this attribute to another class, e.g: BankingService
        self.client_service = client_service or ClientService()

        # self._interface = get_interface()

    @property
    def settings(self) -> Settings:
        return self._settings

    @property
    def interface(self):
        return self.settings.interface

    def startup(self) -> None:
        print("Executing app-specific startup logic..")

    def run(self) -> None:
        print("Application running...")

        print("User Interface %r is loaded." % self.settings.interface.type)

    def exit(self) -> None:
        print("Executing app-specific exit logic..")

    # TODO: Remove this test method to another class, e.g: BankingService
    def create_client(self):
        print("Client creation requested from App...")

        client = self.client_service.create("Test Client-1")

        return client
