from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, TypeVar

from banking.config import get_settings

if TYPE_CHECKING:
    from banking.config import Settings


class BackendProto(Protocol):
    backend: str


BackendT = TypeVar("BackendT", bound=BackendProto)

AppBackendT = TypeVar("AppBackendT", bound=None)
StorageBackendT = TypeVar("StorageBackendT", bound=None)


_APP_BACKENDS: dict[str, AppBackendT] = {}

_STORAGE_BACKENDS: dict[str, StorageBackendT] = {}


def _read_from_config(settings: Settings, attname: str) -> str:
    if not hasattr(settings, attname):
        raise TypeError("Invalid settings, does not have attr: %r" % attname)

    return getattr(settings, attname).backend


class Factory:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def settings(self) -> Settings:
        return self._settings

    @property
    def app(self) -> AppBackendT:
        return self._get_app()

    @property
    def storage(self) -> StorageBackendT:
        return self._get_storage()

    def _get_app(self) -> AppBackendT:
        app = _read_from_config(self.settings, attname="app")

        return _APP_BACKENDS[app]

    def _get_storage(self) -> StorageBackendT:
        storage = _read_from_config(self.settings, attname="storage")

        return _STORAGE_BACKENDS[storage]


##################################################################
# PUBLIC API
##################################################################


def get_factory() -> Factory:
    return Factory(settings=get_settings())


"""
Let's say we are within the App.

We have the settings, but App does not have to touch the config. It works with the factory.

So App.factory has the ability to load different types of backends.

app.factory.app -> App Backend
app.factory.storage -> Storage Backend

That way we are then able to load the things within the app from the factory. It is the central place to load the things.

"""
