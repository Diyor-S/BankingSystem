from collections.abc import Sequence
from typing import Any, Protocol, TypeVar, Generic, TypeAlias, Union


class SearchProto(Protocol):
    def get(self, *args: Any, **kwargs: Any) -> Any: ...
    def get_many(self, *args: Any, **kwargs: Any) -> Any: ...
    def get_all(self, *args: Any, **kwargs: Any) -> Any: ...


class StorageProto(SearchProto, Protocol):
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def delete(self, *args: Any, **kwargs: Any) -> Any: ...
    def update(self, *args: Any, **kwargs: Any) -> Any: ...

EntityID: TypeAlias = Union[int, str]

class EntityProto(Protocol):
    id: EntityID


EntityClassT = TypeVar("EntityClassT", bound=type)
EntityT = TypeVar("EntityT", bound=EntityProto)


class Storage(Generic[EntityClassT]):
    storage: Any

    def __init__(self, entity_cls: EntityClassT) -> None:
        self.entity_class = entity_cls

    def create(self, *args,  **kwargs) -> EntityT:
        raise NotImplementedError

    def update(self, *args, **kwargs) -> EntityT:
        raise NotImplementedError

    def delete(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def get(self, *args, **kwargs) -> EntityT:
        raise NotImplementedError

    def get_many(self, number: int) -> Sequence[EntityT]:
        raise NotImplementedError

    def get_all(self) -> Any:
        raise NotImplementedError

