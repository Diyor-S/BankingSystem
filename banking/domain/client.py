class Person:
    """
    Person - base class for defining a Person.

    Foundation for Client class.

    Inherits: None.
    """

    def __init__(self, first_name: str, last_name: str, identity: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._identity = identity

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def identity(self) -> str:
        return self._identity

    def __repr__(self) -> str:
        return f"{type(self).__name__}(full_name={self.full_name}, id={self.identity})"

class Client:
    """
    Client - core entity of the Banking System.

    Inherits: Person class.
        Inherited attributes:

    """

    def __init__(self, name: str, email: str, password: str) -> None:
        """


        :param name:
        :param email:
        :param password:
        """
