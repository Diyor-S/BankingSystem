"""
Core constants of Banking System.
"""

PASSPORT_SECRET = "passportpassword"

ACCOUNT_SECRET = "accountpassword"

BANK_SECRET = "bankpassword"

UI_IMPL: dict[str, type] = {
    "web": ...,
    "cli": ...,
    "gui": ...
}