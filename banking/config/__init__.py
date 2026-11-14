"""
Application Configuration.
"""

import os
from functools import cache

from dotenv import load_dotenv

load_dotenv()

APP_BACKENDS = {
    "cli": "banking.adapters.cli.Cli",
    "web": "banking.adapters.web.Web",
    "gui": "banking.adapters.gui.Gui"
}

STORAGE_BACKENDS = {
    "inmemory": "banking.repositories.storage.inmemory.InMemoryStorage",
    "database": "banking.repositories.storage.database.DatabaseStorage",
    "file": "banking.repositories.storage.database.FileStorage",
}

class AppNotSupported(Exception): ...
class StorageNotSupported(Exception): ...


class ApplicationConfig:
    def __init__(self, backend_module: str) -> None:
        self.backend = backend_module

class StorageConfig:
    def __init__(self, backend_module: str):
        self.backend = backend_module


class Settings:
    def __init__(self):
        self.app = ApplicationConfig(backend_module=get_app())
        self.storage = StorageConfig(backend_module=get_storage())


def get_app() -> str:
    backend = os.getenv("APP") or "web"

    if backend not in APP_BACKENDS:
        raise AppNotSupported("App type: %r is not supported!" % backend)

    return APP_BACKENDS[backend]

def get_storage() -> str :
    backend = os.getenv("STORAGE") or "database"

    if backend not in STORAGE_BACKENDS:
        raise StorageNotSupported("Storage type: %r is not supported!" % backend)

    return STORAGE_BACKENDS[backend]


@cache
def get_settings():
    return Settings()