"""
Application Configuration.
"""

from typing import Literal
from functools import cache


class ApplicationConfig:
    backend: Literal[
        "cli",
        "web",
        "gui"
    ]

class StorageConfig:
    backend = Literal[
        "inmemory",
        "file",
        "database"
    ]


class Settings:
    def __init__(self):
        self.app = ApplicationConfig()
        self.storage = StorageConfig()


@cache
def get_settings():
    return Settings()