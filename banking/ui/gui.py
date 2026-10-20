class Gui:
    name = "gui"
    commands = None

    def startup(self) -> None:
        pass

    def run(self) -> None:
        pass

    def shutdown(self) -> None:
        pass

    def support_desktop_method(self):
        print("Testing Desktop specific method support for UIHandler scalability support.")