from __future__ import annotations

from typing import TYPE_CHECKING

from banking.repositories import ClientRepository

if TYPE_CHECKING:
    from banking.core.client import Client


class ClientService:
    def __init__(self, client_repository: ClientRepository | None = None) -> None:
        self.client_repository = client_repository or ClientRepository()

    def create(self, name: str) -> Client:
        client = self.client_repository.create(name=name)

        print(
            "New client: %r, "
            "has been successfully created within the system!" % client
        )

        return client
