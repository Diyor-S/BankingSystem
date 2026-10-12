from __future__ import annotations

from collections.abc import Iterator, MutableMapping, MutableSet
from typing import TYPE_CHECKING, Any, Protocol, Self

if TYPE_CHECKING:
    from app import BankingSystem as App


class Group:
    COMMANDS: Group
    """Default group for user-provided commands"""
    HELP: Group
    """Help commands"""

    def __init__(
        self,
        text: str,
        *,
        parent: Group | None = None,
        section: int = 0,
        order: int = 0,
        id_: str | None = None,
    ) -> None:
        self.id_ = f"group-{id(self)}" if id_ is None else id_
        self._text = text
        self.order = order

        if parent is None and section != 0:
            raise ValueError("Section can't be created without parent group")

        self.section = section

        self._parent: Group | None = None
        self.parent = parent

    @property
    def text(self) -> str:
        return self._text

    @property
    def parent(self) -> Group | None:
        return self._parent

    @parent.setter
    def parent(self, parent: Group | None) -> None:
        if parent is None:
            self._parent = None
        elif parent == self:
            raise ValueError("The same group can't be a parent of itself")
        elif self.is_parent_of(parent):
            raise ValueError(
                f"Can not set parent; {self.text!r} is an ancestor of the {parent.text!r}"
            )
        else:
            self._parent = parent

    @property
    def root(self) -> Group:
        parent = self.parent

        if parent is None:
            return self

        return parent.root

    def is_parent_of(self, child: Group | None) -> bool:
        if child is None:
            return False
        if child.parent is None:
            return False

        if child.parent == self:
            return True

        return self.is_parent_of(child.parent)

    def is_child_of(self, parent: Group | None) -> bool:
        if parent is None:
            return False

        return parent.is_parent_of(self)


Group.HELP = Group("Help", order=1)
Group.COMMANDS = Group("Commands", order=2)


class ActionHandler(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...


class Command:
    ABOUT: str = "about"
    EXIT: str = "exit"
    DEPOSIT: str = "accounts.deposit"
    WITHDRAW: str = "accounts.withdraw"

    def __init__(
        self,
        text: str,
        shortcut: str,
        *,
        action: ActionHandler | None,
        arguments: tuple[Argument, ...] | None,
        group: Group = Group.COMMANDS,
        section: int = 0,
        order: int = 0,
        id_: str | None = None,
    ) -> None:
        self.id_ = f"cmd-{id(self)}" if id_ is None else id_
        self._text = text
        self._shortcut = shortcut

        self._action = action
        self._arguments = arguments
        self.group = group

        self.section = section
        self.order = order

    @property
    def arguments(self) -> tuple[Argument, ...] | None:
        return self._arguments

    @property
    def shortcut(self) -> str:
        return self._shortcut

    @property
    def text(self) -> str:
        return self._text

    @classmethod
    def standard(cls, app: App, command_id: str, **kwargs: Any) -> Self:
        metadata = STANDARD_COMMANDS[command_id]

        try:
            attrs = command_id.split(".")
            action = getattr(app, attrs[0])

            for attr in attrs[1:]:
                action = getattr(action, attr)
        except AttributeError:
            action = None

        essential_kwargs = {
            "action": action,
            "id_": command_id,
            "arguments": metadata["arguments"],
        }

        return cls(metadata["text"], metadata["shortcut"], **essential_kwargs, **kwargs)

    def execute(self, *args) -> None:
        if self._action is not None:
            self._action(*args)

    def describe(self) -> str:
        lines = [
            f"  {self.text}",
        ]

        if self.shortcut:
            lines.append(f"    Shortcut: {self.shortcut}")

        return "\n".join(lines)


class Argument:
    def __init__(self, name: str, type_: type) -> None:
        self.name = name
        self._type = type_

    @property
    def type(self) -> type:
        return self._type

    def parse(self, value):
        return self.type(value)


STANDARD_COMMANDS = {
    Command.ABOUT: {"text": "About", "shortcut": "1", "arguments": None},
    Command.EXIT: {"text": "Exit", "shortcut": "q", "arguments": None},
    Command.DEPOSIT: {
        "text": "Deposit",
        "shortcut": "2",
        "arguments": (Argument("account_id", int), Argument("amount", int)),
    },
    Command.WITHDRAW: {
        "text": "Withdraw",
        "shortcut": "3",
        "arguments": (Argument("account_id", int), Argument("amount", int)),
    },
}


class CommandSet(MutableMapping[str, Command], MutableSet[Command]):
    def __init__(self, app: App | None = None) -> None:
        self._app: App | None = app
        self._commands: dict[str, Command] = {}

    def __getitem__(self, id_: str) -> Command:
        return self._commands[id_]

    def __setitem__(self, id_: str, command: Command) -> None:
        if id_ != command.id_:
            raise ValueError(f"Command has id {command.id_}!r, can't add as {id_}!r")

        self.add(command)

    def __delitem__(self, id_: str) -> None:
        del self._commands[id_]

    def __iter__(self) -> Iterator[str]:
        return iter(self._commands.keys())

    def __len__(self) -> int:
        return len(self._commands)

    @property
    def app(self) -> App | None:
        return self._app

    def add(self, *commands: Command | None) -> None:
        app = self.app

        for command in commands:
            if not isinstance(command, Command):
                raise TypeError(f"Command {command!r} is not a Command")

        if app:
            app.commands.add(*commands)

        self._commands.update({cmd.id_: cmd for cmd in commands if cmd is not None})

    def discard(self, command: Command) -> None:
        try:
            self._commands.pop(command.id_)
        except KeyError:
            pass

    def clear(self) -> None:
        self._commands.clear()

    def get_by_shortcut(self, shortcut: str) -> Command:
        for command in self._commands.values():
            if command.shortcut == shortcut:
                return command
        raise ValueError(f"Command with shortcut {shortcut!r} not found")
