"""
Core Validators of Banking System.
"""

import re
from typing import (
    Any,
    Callable,

)
from functools import wraps


class PermissionDenied(Exception):
    pass


def require_password(password_: str) -> Callable:
    def decorator(handler: Callable) -> Callable:
        @wraps(handler)
        def wrapper(*args, **kwargs) -> Any:
            """
            First Solution that triggered Pycharm Warning: Missing return statement on some paths:

            if user_password == password_:
                print("Password Matched, invoking the handler...")
                return handler(*args, **kwargs)

            attempts = 2

            while attempts > 0:
                user_password = input(f"Attempts left: {attempts}.\nEnter the correct password: ")

                if user_password != password_:
                    attempts -= 1
                    continue

                print("Password Matched, invoking the handler...")
                return handler(*args, **kwargs)

            if attempts <= 0:
                raise PermissionDenied("Max attempts reached. Handler Invocation cancelled!")
            """
            max_attempts = 3

            for attempt in range(max_attempts):
                if attempt == 0:
                    user_password = input("Enter the password to perform the operation: ")
                else:
                    attempts_left = max_attempts - attempt
                    user_password = input(f"Attempts left: {attempts_left}.\nEnter the correct password: ")

                if user_password == password_:
                    return handler(*args, **kwargs)

            raise PermissionDenied("Max attempts reached.")

        return wrapper

    return decorator


PassportValidator = re.compile('^[A-Za-z]{2}\d{7}$')


