"""
Application Configuration.
"""

from functools import cache

_UIs: dict[str, str] = {
    "cli": "cli",
    "web": "web",
}

class UserInterfaceConfig:
    type: str = _UIs["cli"]

class Settings:
    def __init__(self):
        self.interface = UserInterfaceConfig()


@cache
def get_settings():
    return Settings()