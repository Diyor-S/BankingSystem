from .base import RunConfig

class WebRunConfig(RunConfig):
    """
    Web application configuration.

    host: server's host
    port: server's running port number
    """
    key = "web"

    host: str = "0.0.0.0"
    port: int = 8080

class WebConfig:
    pass

