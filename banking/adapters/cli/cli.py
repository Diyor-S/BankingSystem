"""
Cli-based user interface.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .command import CommandSet

if TYPE_CHECKING:
    from banking.app import App


class Cli:
    def __init__(self, app: App) -> None:
        self._app = app

        self._commands = CommandSet()

    @property
    def app(self) -> App:
        return self._app

    @property
    def commands(self) -> CommandSet:
        return self._commands

    def run(self) -> None:
        print("Hello from Cli adapter!")

        self.startup()

        try:
            while True:
                message = input("Enter your command: ")

                if message == "1":
                    client = self.app.create_client()

                    all_clients = self.app.client_service.get_all()

                    print("Welcome client: %r" % client.name)

                    print("These are all clients that we have got already: %s" % all_clients)

                print("Your message: %r" % message)
        except KeyboardInterrupt:
            print("\nShutdown triggered!")
            self.exit()

    def startup(self) -> None:
        print("Cli app is starting up...")

        print("Initializing Application-Specific state")
        self.app.startup()

    def exit(self) -> None:
        print("Cli app is shutting down...")

        print("Invoking app-specific cleanup...")
        self.app.exit()
