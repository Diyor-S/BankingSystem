"""
Main Entrypoint to the Application.
"""

from app import App
from adapters import Cli, Web

if __name__ == "__main__":
    app = App()

    # cli = Cli(app=app)
    # cli.run()

    web = Web(app=app)
    web.run()