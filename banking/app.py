"""
Application implementation for Banking System.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from banking.config import get_settings
from banking.factory import get_factory
from banking.services import ClientService

if TYPE_CHECKING:
    from banking.config import Settings
    from banking.factory import Factory


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

        self._factory = get_factory()

    @property
    def settings(self) -> Settings:
        return self._settings

    @property
    def factory(self) -> Factory:
        return self._factory

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
