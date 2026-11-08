class Client:
    def __init__(self, name: str = "David"):
        # Let id be memory address of an instance for now.
        self.id = id(self)
        self.name = name

    def __repr__(self) -> str:
        return f"Client(id='{self.id}', name='{self.name}')"
