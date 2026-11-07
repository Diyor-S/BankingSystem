from __future__ import annotations

import copy
import enum
import itertools
from typing import Any, TypeVar
from collections.abc import Sequence

from .base import EntityID, EntityT, EntityClassT
from .base import Storage

class EntityNotFound(Exception):
    pass

class SelectionMode(enum.Enum):
    LAST = -1
    FIRST = 0

StorageT = TypeVar("StorageT", bound=Any)

class InMemoryStorage(Storage[EntityClassT]):
    def __init__(self, entity_cls: EntityClassT) -> None:
        super().__init__(entity_cls)

        self._storage: dict[EntityID, EntityT] = {}                       # noqa

    @property
    def storage(self) -> StorageT:
        return self._storage

    def _get_entity(self, entity_id: EntityID) -> EntityT:
        try:
            return self.storage[entity_id]
        except KeyError:
            raise EntityNotFound("Entity with id: %r does not exist" % entity_id)

    def create(self, *args, **kwargs) -> EntityT:
        entity = self.entity_class(*args, **kwargs)

        self.storage[entity.id] = entity

        return copy.deepcopy(entity)

    def update(self, entity_id: EntityID, **kwargs: Any) -> EntityT:

        entity = self._get_entity(entity_id)

        for key, value in kwargs.items():
            try:
                setattr(entity, key, value)
            except AttributeError:
                raise AttributeError("Entity: %s does not have attribute %r to set value %r" % (entity, key, value))

        return entity

    def delete(self, entity_id: EntityID) -> None:
        entity = self._get_entity(entity_id)

        del self.storage[entity.id]

    def get(self, entity_id: EntityID) -> EntityT:
        return copy.deepcopy(self._get_entity(entity_id))

    def get_many(self, number: int, which: SelectionMode = SelectionMode.FIRST, sorting_condition=None) -> Sequence[EntityT]:
        iterable_ = self.storage.values()

        if which is SelectionMode.LAST:
            reversed_iterable = reversed(iterable_)
            result = list(itertools.islice(reversed_iterable, number))

            return copy.deepcopy(result)

        return copy.deepcopy(list(itertools.islice(iterable_, number)))

    def get_all(self) -> Sequence[EntityT]:
        return copy.deepcopy(list(self.storage.values()))
