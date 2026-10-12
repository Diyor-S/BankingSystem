"""
Core Banking System exceptions.
"""

### ===========================================================================
## Generic Exceptions
### ===========================================================================

class NameValidationError(Exception):
    pass

class CommandNotFoundByID(Exception):
    pass

### ===========================================================================
## Passport Exceptions
### ===========================================================================


class PassportValidationFailed(Exception):
    pass


### ===========================================================================
## Account Exceptions
### ===========================================================================


# Transaction Exceptions

class NoSuchTransactionMethod(Exception):
    pass

class TransactionError(Exception):
    pass


# Deposit/Withdrawal decline Exceptions

class DepositDeclined(Exception):
    pass

class WithdrawDeclined(Exception):
    pass

class NotEnoughMoneyToWithdraw(Exception):
    pass


