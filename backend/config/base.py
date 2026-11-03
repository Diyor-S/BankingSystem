"""
Base configuration for all different kinds of application config.
"""

import enum
from typing import Self, Callable


class ApplicationType(enum.Enum):
    WEB = "web"
    CLI = "cli"
    GUI = "gui"

class ConfigType(enum.Enum):
    RUN = "run"

class ConfigRegisterMixin:
    def __init_subclass__(cls, **kwargs):
        key = kwargs.pop("key", None)

        if not key:
            raise TypeError("Keyword argument 'key' MUST be passed during class definition")

        config_types = {}

        for attr in cls.__dict__:
            if not hasattr(attr, "key"):
                continue
            config_types[attr.key] = attr.get_registry()

        ConfigRegistry[key] = cls

        super().__init_subclass__(cls, **kwargs)



class RunConfig:
    """
    Application run configuration.
    """

    key: str

    _registry: dict[str, Self] = {}

    def __init_subclass__(cls):
        cls._registry[cls.key] = cls()

        super().__init_subclass__(cls)

    @classmethod
    def get_enabled(cls) -> Self:
        """
        Environment variable `run` should be present.
        Retrieve based on that exact string name of the run.

        :return: BaseRunConfig instance.
        """

        import os

        run = os.getenv("RUN", "cli")

        return cls._registry[run]

    def setup(self) -> None:
        """
        Subclasses should override this method to set up their own way.

        E.g.:
        web might need to set up the server.
        cli does not need any of that.

        :return:
        """

class FileConfig:
    pass

class DBConfig:
    pass

class BaseConfig:
    run: RunConfig
    db: DBConfig | None = None
    file: FileConfig | None = None

    def setup(self):
        """
        Subclasses should override this method to automate the configuration process for a particular backend.

        :return:
        """

    @property
    def has_setup(self) -> bool:
        return type(self).setup is not BaseConfig.setup


# ConfigRegistry: dict[str, dict[str, type]]
# ConfigRegistry["run"]["web"] or ConfigRegistry["run"]["cli"] or ConfigRegistry["run"]["gui"]
# ConfigRegistry["web"]["run"] or ConfigRegistry["cli"]["run"] or ConfigRegistry["gui"]["run"]
# The second option is better I think, we have identical public interface.

ConfigRegistry: dict[
    ApplicationType,
    dict[ConfigType, BaseConfig]
] = {}
