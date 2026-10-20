

class Field:
    default_validators = []
    default_error_messages = []

    def __init__(self, value, *,  validators=(), errors=None) -> None:
        self._validators = validators
        self._error_messages = errors

    @property
    def error_messages(self):
        pass

    @property
    def validators(self):
        pass

    def extend(self) -> None:
        pass


class StrField(Field):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class IntegerField(Field):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class BooleanField(Field):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class DateField(Field):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Model:
    _fields: dict[str, Field] = {}

    def __init__(self, *args, **kwargs) -> None:
        """
        Two cases:

        Model receiving only args, maybe leftovers -> kwargs with default values
        Model receiving only kwargs, maybe leftovers -> kwargs with default values.

        Use only one: either only args, or only kwargs, not both.

        :param args:
        :param kwargs:
        """

        if len(args) > len(self._fields):
            raise TypeError("The number of arguments exceeds the number of fields")


        if not kwargs:
            fields_iter = iter(self._fields.values())

            for value, field in zip(args, fields_iter):
                setattr(self, field.name, value)

class ModelOptions:
    pass

class Passport:
    name = StrField(length=200)
    expires_at = DateField()

"""
What we need to do is:

Some Model -> Entity of Banking System
We should use the Metaclass, to wrap those Entity attributes within the Metaclass

That metaclass should be injecting and wrapping each attribute with the Field, of the corresponding type I suppose.
No that would be adding extra things to check again. 

Better if we just use those straight awa and also if our Field already infers the type based on the usage of the Field.

Because, what we would be getting at:
We would be making the end user use those Fields, while the type would be already inferred by the Field.
We would just be passing the value to the field that it would have to validate. 

After we reach that, how should the behavior actually be?
What do we want even to achieve?

>>> Model.name -> that would be the Field instance, so when the __getattribute__ is invoked it should be returning the 
value that it has.

>>> Model().name => Field().value
"""


class UIMetaclass(type):
    def __new__(mcls, name, bases, attrs) -> type:
        new_class = super().__new__(mcls, name, bases, attrs)

        return new_class



class UIScanning(metaclass=UIMetaclass):
    pass
