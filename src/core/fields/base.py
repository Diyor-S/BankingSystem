class Field:
    def __init__(self):
        pass

    def __set_name__(self, owner, name) -> None:
        self.public = name
        self.private = "_" + name

    def __get__(self, obj, owner=None):
        if obj is not None:
            raise TypeError("Only class-based access is allowed")

        return getattr(owner, self.private)



class UIMetaclass(type):
    def __new__(mcls, name, bases, attrs) -> type:
        new_class = super().__new__(mcls, name, bases, attrs)

        return new_class



class UIScanning(metaclass=UIMetaclass):
    pass
