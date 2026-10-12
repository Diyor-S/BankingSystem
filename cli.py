from __future__ import annotations

import time
from datetime import date
from enum import StrEnum
from typing import TYPE_CHECKING

from client import Client
from account import UZBAccount
from passport import UZBPassport

if TYPE_CHECKING:
    from app import BankingSystem as App

def startup_ui() -> None:
    linear_separator()

    print("You may interact with the CLI.\n")
    print("Press CTRL + C to exit.")

    linear_separator()

def show_commands(app: "App") -> None:
    eq_separator()
    print("Commands:")

    for command in app.commands.values():
        print(f"{command.shortcut:>2}  {command.text}")


def shutdown_ui() -> None:
    linear_separator()

    print("Application exiting...")
    # time.sleep(2)

    print("Application cleanup complete")
    print("Application shutdown")

    eq_separator()


def eq_separator() -> None:
    print("==============================================")

def linear_separator() -> None:
    print("----------------------------------------------")


def pre_computed() -> tuple[Client, UZBAccount, UZBPassport]:
    passport = UZBPassport(
        first_name="Diyor",
        last_name="Saidaliyev",
        date_of_birth=date(2006, 11, 15),
        expiry_date=date(2030, 11, 15),
        identifier="AD2085496"
    )

    account = UZBAccount()

    client = Client(
        passport,
        account
    )

    return client, account, passport

def identify_user():
    first_name = input("Enter your name:\n> ")
    last_name = input("Enter your last name:\n> ")

    birth_year = int(input("Enter your birth year:\n> "))
    birth_month = int(input("Enter your birth month:\n> "))
    birth_day = int(input("Enter your birth day:\n> "))

    expiry_year = int(input("Enter your passport's expiry year:\n> "))
    expiry_month = int(input("Enter your passport's expiry month:\n> "))
    expiry_day = int(input("Enter your passport's expiry day:\n> "))

    identifier = input("Enter your passport's identifier:\n> ")

    birth_date = date(birth_year, birth_month, birth_day)
    expiry_date = date(expiry_year, expiry_month, expiry_day)

    passport = UZBPassport(
        first_name,
        last_name,
        birth_date,
        expiry_date,
        identifier
    )

    account = UZBAccount()

    client = Client(
        passport,
        account
    )

    return client, account, passport


# Utility UI functions

def line() -> None:
    print("----------------------------------------------")

def equal() -> None:
    print("==============================================")

class InputHandler:
    def validate(self, type_: Any, value: Any) -> None:
        pass



# StartUp and Shutdown Handler Mixin

class LifespanUIMixin(InputHandler):
    mode: UIDataMode

    def startup(self) -> None:
        pass

    def shutdown(self) -> None:
        pass

    def _pre_computed(self) -> None:
        pass

    def require_data(self) -> None:
        pass


class CommandUIMixin:
    app: "App"

    def show_commands(self) -> None:
        eq_separator()
        print("Commands:")

        for command in self.app.commands.values():
            print(f"{command.shortcut:>2}  {command.text}")

class AccountUIMixin:
    pass

class PassportUIMixin:
    pass

class UserUIMixin(PassportUIMixin, AccountUIMixin):
    pass

class UIDataMode(StrEnum):
    MOCK = "MOCK"
    REQUIRE = "REQUIRE"

class UIHandler(LifespanUIMixin, UserUIMixin, CommandUIMixin):
    def __init__(self, app: App, mode: UIDataMode = UIDataMode.MOCK) -> None:
        self._app = app
        self._data_mode = mode

    @property
    def data_mode(self) -> UIDataMode:
        return self._data_mode

    @property
    def app(self) -> App:
        return self._app

    def show_default(self) -> None:
        pass

