from __future__ import annotations

from typing import Protocol

class UIProto(Protocol):
    """
    User Interface Protocol.

    At least has to have: startup, run, and shutdown.

    For now let be it, but we might remove 'run' later.

    Moreover, we would need to consider what other attributes are 'essential'.
    We must not enforce the attributes that are in some subclasses, while in others not present.

    Example: 'commands' attribute, not all user interfaces might have this attribute.
    Enforcing this attribute in this Protocol makes the ones that do not have incompatible with this type.
    """
    commands: None

    def startup(self) -> None: ...
    def run(self) -> None: ...
    def shutdown(self) -> None: ...
