"""
Application Configuration.
"""

import os
from functools import cache

from dotenv import load_dotenv

load_dotenv()

APP_BACKENDS = ("cli", "web", "gui")
STORAGE_BACKENDS = ("inmemory", "file", "database")

class AppNotSupported(Exception): ...
class StorageNotSupported(Exception): ...


class ApplicationConfig:
    def __init__(self, backend_name: str) -> None:
        self.backend = backend_name

class StorageConfig:
    def __init__(self, backend_name: str):
        self.backend = backend_name


class Settings:
    def __init__(self):
        self.app = ApplicationConfig(backend_name=get_app())
        self.storage = StorageConfig(backend_name=get_storage())


def get_app() -> str:
    backend = os.getenv("APP") or "web"

    if backend not in APP_BACKENDS:
        raise AppNotSupported("App type: %r is not supported!" % backend)

    return backend

def get_storage() -> str :
    backend = os.getenv("STORAGE") or "database"

    if backend not in STORAGE_BACKENDS:
        raise StorageNotSupported("Storage type: %r is not supported!" % backend)

    return backend


@cache
def get_settings():
    return Settings()