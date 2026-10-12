class Bank:
    def __init__(
        self,
        name: str,
        address: str,
        *,
        is_main: bool = False,
    ) -> None:
        self.name = name
        self.address = address

        self._is_main = False
        self.is_main = is_main

        self._cards = None
        self._clients = None
        self._accounts = None
        self._passports = None


    @property
    def is_main(self) -> bool:
        """
        Is this bank the main branch?

        :return: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, value: bool) -> None:
        """
        Setter for the main branch or not branch.

        :param value: boolean to set the main branch True or False
        :return: None
        """
        if not isinstance(value, bool):
            raise TypeError("Must be of type bool")

        self._is_main = value


    def startup(self) -> None:
        """
        Actions to perform on Backend Startup.

        Maybe initialize some attributes, create some records, admin related things.

        :return:
        """
        pass

    def shutdown(self) -> None:
        """
        Actions to perform on Backend Shutdown.

        Maybe perform some cleanup logic, release some resources, very abstract for now.

        :return:
        """
        pass