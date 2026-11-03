"""
Main Entrypoint to the Banking System Application.
"""

from app import App
from config.settings import settings

if __name__ == "__main__":
    # Initialize application instance
    # with corresponding configuration.
    app = App(settings)

    # Run application, the running method should be
    # automatically inferred from settings.
    app.run()
