from __future__ import annotations

from domain.bank import Bank
from ui.base import UIProto, UIHandler
from config.constants import UI_IMPL


class UserInterfaceNotSupported(Exception):
    pass

class App:
    def __init__(self, bank: Bank | None = None, ui: UIProto | None = None) -> None:
        self._bank = bank or Bank("SmartBank", "Tashkent")

        if ui is not None:
            if not isinstance(ui, UIProto):
                raise TypeError("Invalid UI interface received. It should satisfy the UIProto interface!")

            if ui.name not in UI_IMPL:
                raise UserInterfaceNotSupported("Implementation for this User Interface not supported")
        else:
            ui = UI_IMPL.get("cli")()


        self._ui = UIHandler(ui)

    @property
    def bank(self) -> Bank:
        """
        Bank instance reference that holds Bank State.

        :return: reference to Bank instance.
        """
        return self._bank

    @property
    def ui(self) -> UIProto:
        """
        User Interface property - Read-Only Descriptor.

        :return: reference to User Interface instance.
        """
        return self._ui

    @property
    def commands(self) -> ... | None:
        """
        Application Commands.
        Taken from UI if it has 'commands' attribute. They are Optional.

        :return: reference to Commands instance.
        """
        return self.ui.commands if self.are_commands_supported else None

    @property
    def are_commands_supported(self) -> bool:
        """
        Are commands supported for this User Interface?

        :param ui: current User Interface.
        :return: True if we get from 'ui' attribute 'commands' to be other than 'None' else False.
        """
        commands = getattr(self.ui, "commands", None)
        return commands is not None

    def run(self) -> None:
        """
        Main Application Loop.
        Performs all the required preparations and cleanup.

        :return: None
        """
        print("App is running...")

        self.ui.startup()

