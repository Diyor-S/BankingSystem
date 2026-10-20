class Cli:
    name = "cli"
    commands: None

    def startup(self) -> None:
        print("This is the cli startup UI method invoked!")

    def run(self) -> None:
        print("This is the cli running, keeps running.")

    def shutdown(self) -> None:
        pass

    def support_cli_method(self):
        print("Testing CommandLineInterface specific method support for UIHandler scalability support.")