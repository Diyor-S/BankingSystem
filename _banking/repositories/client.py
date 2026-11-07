"""Client Repository implementation."""

from typing import Any, TypeAlias

from _banking.core.client import Client

ClientID: TypeAlias = str
ClientSet: TypeAlias = dict[ClientID, Client]

class ClientRepository:
    """
    Client Repository, internal operations perform with client.
    """

    def __init__(self) -> None:
        self.clients: ClientSet = {}

    def create(self, **kwargs: Any) -> Client:
        client = Client(**kwargs)

        self.clients[client.id] = client

        return client

    def get(self, client_id: ClientID) -> Client | None:
        try:
            return self.clients[client_id]
        except KeyError:
            return None

    def all(self) -> ClientSet:
        pass