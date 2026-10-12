from app import App
from ui.cli import Cli
from domain.bank import Bank


def main() -> None:
    app = App()
    app.run()

if __name__ == "__main__":
    main()