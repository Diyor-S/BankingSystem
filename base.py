from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Iterator,
    Protocol,
)


class EntityProto(Protocol):
    @property
    def id_(self) -> Any: ...

EntityID = TypeVar("EntityID")
EntityT = TypeVar("EntityT", bound=EntityProto)

class BaseMapping(Mapping[EntityID, EntityT]):
    entity_class: type[EntityT]

    def __init__(self) -> None:
        self._items: dict[EntityID, EntityT] = {}

    def __getitem__(self, key: EntityID) -> EntityT:
        return self._items[key]

    def __iter__(self) -> Iterator[EntityID]:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    # Set like behavior add/remove

    def add(self, item: EntityT) -> None:
        if not isinstance(item, self.entity_class):
            raise TypeError(f"Item {item} is not of type {self.entity_class.__name__}!")

        self._items[item.id_] = item

    def remove(self, item: EntityT) -> None:
        if not isinstance(item, self.entity_class):
            raise TypeError(f"Item {item} is not of type {self.entity_class.__name__}!")

        if item.id_ not in self._items:
            raise ValueError(f"No such item: {item} to remove!")

        self._items.pop(item.id_)

    def find_by_id(self, item_id: EntityID) -> EntityT | None:
        try:
            return self._items[item_id]
        except KeyError:
            return None


