from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any, TypeVar, Generic, Protocol

class EntityProto(Protocol):
    @property
    def id(self) -> Any: ...

EntityT = TypeVar("EntityT", bound=EntityProto)
EntityID = TypeVar("EntityID")


class Storage(ABC, Generic[EntityID, EntityT]):
    @abstractmethod
    def add(self, item: EntityT) -> None:
        pass

    @abstractmethod
    def delete(self, item: EntityT) -> None:
        pass

    @abstractmethod
    def update(self, item: EntityT) -> None:
        pass

    @abstractmethod
    def all(self) -> Sequence[EntityT]:
        pass

    def get(self, item_id: EntityID) -> EntityT | None:
        return next((item for item in self.all() if item.id == item_id), None)

class InMemoryStorage(Storage[EntityID, EntityT]):
    def __init__(self) -> None:
        self._items: dict[EntityID, EntityT] = {}

    def add(self, item: EntityT) -> None:
        self._items[item.id] = item

    def delete(self, item: EntityT) -> None:
        del self._items[item.id]

    def update(self, item: EntityT) -> None:
        self._items[item.id] = item

    def all(self) -> Sequence[EntityT]:
        return list(self._items.values())


class FileStorage(Storage[EntityID, EntityT]):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def add(self, item: EntityT) -> None:
        pass

    def delete(self, item: EntityT) -> None:
        pass

    def update(self, item: EntityT) -> None:
        pass

    def all(self) -> Sequence[EntityT]:
        pass


class DatabaseStorage(Storage[EntityID, EntityT]):
    def __init__(self, database_url: str) -> None:
        self.url = database_url

    def add(self, item: EntityT) -> None:
        pass

    def delete(self, item: EntityT) -> None:
        pass

    def update(self, item: EntityT) -> None:
        pass

    def all(self) -> Sequence[EntityT]:
        pass


