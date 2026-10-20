"""
Core constants of Banking System.
"""

from ui.cli import Cli
from ui.gui import Gui
from ui.rest import RestAPI

PASSPORT_SECRET = "passportpassword"

ACCOUNT_SECRET = "accountpassword"

BANK_SECRET = "bankpassword"

UI_IMPL: dict[str, type] = {
    "web": RestAPI,
    "cli": Cli,
    "gui": Gui
}