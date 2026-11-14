"""
Main Entrypoint to the Application.
"""

import importlib

from banking.app import App
from banking.config import get_settings
from banking.core.client import Client
from banking.repositories.client import ClientRepository
from banking.services.client import ClientService

def _load_backends() -> tuple[type, ...]:
    settings = get_settings()

    app_module, _, app_class = settings.app.backend.rpartition(".")
    storage_module, _, storage_class = settings.storage.backend.rpartition(".")

    app_backend_module = importlib.import_module(app_module)

    storage_backend_module = importlib.import_module(storage_module)

    app_class = getattr(app_backend_module, app_class)
    storage_class = getattr(storage_backend_module, storage_class)

    return app_class, storage_class


if __name__ == "__main__":
    # TODO: Refactor this module properly to clean it up.

    # Load App and Storage Backends from config
    app_cls, storage_cls = _load_backends()

    # Create core App.
    app = App(client_service=ClientService(ClientRepository(storage_cls(Client))))

    # Create representation of that core App as main_app, typically either Cli or Web.
    main_app = app_cls(app)
    main_app.run()
