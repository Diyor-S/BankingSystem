from __future__ import annotations

from domain.bank import Bank
from ui.base import UIProto
from config.constants import UI_IMPL


class App:
    def __init__(self, bank: Bank | None = None, ui: UIProto | None = None) -> None:
        self._bank = bank or Bank()
        self._ui = ui or UI_IMPL.get("cli")

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
        return self.ui.commands if self.commands_supported(self.ui) else None

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
        Performs all the required preparations and clean-up.

        :return: None
        """
        print("App is running...")

