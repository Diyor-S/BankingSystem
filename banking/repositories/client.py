"""Client Repository implementation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from banking.core.client import Client

from .storage.base import SelectionMode
from .storage.inmemory import EntityNotFound, InMemoryStorage

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any, TypeAlias

    from .storage.base import Storage

    ClientID: TypeAlias = int


class ClientNotFound(Exception):
    pass


class ClientRepository:
    """
    Client Repository, internal operations perform with client.
    """

    def __init__(self, storage: Storage[Client] | None = None) -> None:
        self.clients: Storage[Client] = storage or InMemoryStorage[Client](Client)

    def create(self, **kwargs: Any) -> Client:
        return self.clients.create(**kwargs)

    def update(self, client_id: ClientID, **kwargs) -> Client:
        return self.clients.update(client_id, **kwargs)

    def delete(self, client_id: ClientID) -> None:
        self.clients.delete(client_id)

    def get(self, client_id: ClientID) -> Client | None:
        try:
            return self.clients.get(client_id)
        except EntityNotFound:
            ClientNotFound("Client with id: %r not found." % client_id)

    def get_many(
        self,
        number: int,
        order_by: tuple[str, ...] = (),
        which: SelectionMode = SelectionMode.FIRST,
    ):
        return self.clients.get_many(number, order_by=order_by, which=which)

    def all(self) -> Sequence[Client]:
        return self.clients.get_all()
