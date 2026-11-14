"""
Application implementation for Banking System.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from banking.config import get_settings
from banking.services import ClientService

if TYPE_CHECKING:
    from banking.config import Settings


class App:
    """
    Main class that is an entrypoint to the application.
    """

    def __init__(
        self,
        client_service: ClientService | None = None,
    ) -> None:
        self._settings = get_settings()

        # TODO: Remove this attribute to another class, e.g: BankingService
        self.client_service = client_service or ClientService()

    @property
    def settings(self) -> Settings:
        return self._settings

    def startup(self) -> None:
        print("Executing app-specific startup logic..")

    def run(self) -> None:
        print("Application running...")

    def exit(self) -> None:
        print("Executing app-specific exit logic..")

    # TODO: Remove this test method to another class, e.g: BankingService
    def create_client(self):
        print("Client creation requested from App...")

        client = self.client_service.create("Test Client-1")

        return client
