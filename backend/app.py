from config.settings import Settings

class App:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def settings(self) -> Settings:
        return self._settings

    def startup(self) -> None:
        print("Startup handler is invoked...")

    def exit(self) -> None:
        print("Exit handler is invoked...")

    def run(self) -> None:
        self.startup()

        print("App is running...")

        print("Press CTRL+C to exit.")
        try:
            message = input("Enter your message: ")

            print("Your message: %s" % message)

        except KeyboardInterrupt:
            print("\nThanks for interacting with the application.")
            self.exit()
