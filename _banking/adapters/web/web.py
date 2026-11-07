"""
Web-based user interface.
"""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _banking.app import App


class Web:
    def __init__(self, app: App) -> None:
        self._app = app

    @property
    def app(self) -> App:
        return self._app

    def run(self) -> None:
        print("Hello from Web adapter!")

        self.startup()

        try:
            while True:
                message = input("Enter your message: ")

                print("Your message: %r" % message)
        except KeyboardInterrupt:
            print("\nShutdown triggered!")
            self.exit()

    def startup(self) -> None:
        print("Web app is starting up...")

        print("Initializing application-specific state...")
        self.app.startup()

    def exit(self) -> None:
        print("Web app is shutting down...")

        print("Invoking app-specific cleanup...")
        self.app.exit()