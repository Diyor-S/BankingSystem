from typing import TYPE_CHECKING, TypeAlias

from .base import Storage
from .base import EntityT, EntityClassT

if TYPE_CHECKING:
    DBTableNameT: TypeAlias = str


class DatabaseStorage(Storage[EntityT]):
    url: str = "postgres+"

    def __init__(self, entity_cls: EntityClassT) -> None:
        super().__init__(entity_cls)

        self._storage = self._get_tablename(self.entity_class)

    @property
    def tablename(self) -> DBTableNameT:
        return self._storage

    @staticmethod
    def _get_tablename(entity_cls: EntityClassT) -> str:
        return entity_cls.__name__.lower() + "s"


