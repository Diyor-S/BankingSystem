from typing import Callable

from core.storage import Storage


StorageRegistry: dict[str, Storage] = {
    "clients": ...,
    "accounts": ...,
    "passports": ...,
}

storage_handlers: dict[str, Callable] = {
    "inmemory": ...,
    "file": ...,
    "database": ...,

}

def load_from_config(settings: Settings) -> None:
    storage_mode = getattr(settings, "SMODE")

    try:
        handler = storage_handlers[storage_mode]

        handler(storage_registry=StorageRegistry)

    except KeyError:
        raise KeyError("Storage %s is not supported" % storage_mode)
