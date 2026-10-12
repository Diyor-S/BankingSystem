"""
Main Entrypoint - Banking System.
"""

from __future__ import annotations

import time
from typing import Protocol, Any

from client import Client, ClientSet
from account import UZBAccount, AccountSet
from command import Command, CommandSet, STANDARD_COMMANDS
from passport import UZBPassport, PassportSet

from cli import (
    startup_ui,
    show_commands,
    shutdown_ui,
    eq_separator,
    linear_separator,

    pre_computed,
    identify_user,
)

class OnStartupHandler(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...

class OnExitHandler(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...


class BankingSystem:
    _mock_mode: bool = False

    def __init__(
        self,
        on_startup: OnStartupHandler | None = None,
        on_exit: OnExitHandler | None = None
    ):
        self._clients = ClientSet()
        self._accounts = AccountSet()
        self._passports = PassportSet()

        self._commands = CommandSet()

        self.onstartup = on_startup
        self.onexit = on_exit

    @property
    def clients(self) -> ClientSet:
        return self._clients

    @property
    def accounts(self) -> AccountSet:
        return self._accounts

    @property
    def passports(self) -> PassportSet:
        return self._passports

    @property
    def commands(self) -> CommandSet:
        return self._commands

    def _create_standard_commands(self) -> None:
        for command_id in STANDARD_COMMANDS:
            self.commands.add(Command.standard(self, command_id))

    def about(self) -> None:
        pass

    def _mock_or_interactive(self) -> tuple[Client, UZBAccount, UZBPassport]:
        if self._mock_mode:
            client, account, passport = pre_computed()
        else:
            client, account, passport = identify_user()

        self.passports.add(passport)
        self.accounts.add(account)
        self.clients.add(client)

        return client, account, passport

    def run(self) -> None:
        eq_separator()

        print("Application startup...")
        linear_separator()

        client, account, passport = self.startup()
        startup_ui()

        time.sleep(1.5)

        try:
            while True:
                shortcut = input("Enter the command to execute:\n> ")

                try:
                    command = self.commands.get_by_shortcut(shortcut)
                except KeyError:
                    print(f"Command with shortcut: {shortcut!r} not found")
                    continue
                except ValueError:
                    print(f"Command with shortcut {shortcut!r} not found")
                    continue

                if command.arguments is not None:
                    arguments = []

                    for arg in command.arguments:
                        raw = input(f"{arg.name!r} >> ")

                        try:
                            argument = arg.parse(raw)
                            arguments.append(argument)
                        except ValueError:
                            print(f"Invalid argument for {arg.name!r}, need value compatible with type {arg.type!r}")

                    try:
                        command.execute(*arguments)
                        time.sleep(1.5)
                        client_details(client)
                        time.sleep(1)
                        show_commands(app=self)
                    except Exception as e:
                        print(e)

                else:
                    command.execute()


        except KeyboardInterrupt:
            print("\n")
            shutdown_ui()


    def startup(self) -> tuple[Client, UZBAccount, UZBPassport]:
        print("Let's find out who you are!")

        self._create_standard_commands()

        client, account, passport = self._mock_or_interactive()

        time.sleep(1)
        linear_separator()
        print("Application startup complete.")
        time.sleep(1)

        linear_separator()
        print("Welcome to the Banking System App\n")
        client_details(client)
        show_commands(app=self)

        return client, account, passport


    def exit(self) -> None:
        pass

def client_details(client: Client) -> None:
    print("Client")
    print("------")
    print(f"ID: {client.id_}")
    print(f"Name: {client.fullname}")
    print(f"Age: {client.age}")

    print("\nAccounts")
    print("--------")

    account = client.account
    print(f"ID: {account.id_}")
    print(f"Type: {account.__class__.__name__}")
    print(f"Balance: {account.balance}")

if __name__ == "__main__":
    bank = BankingSystem()

    bank.run()