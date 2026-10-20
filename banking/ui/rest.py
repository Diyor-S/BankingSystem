class RestAPI:
    name = "rest"
    commands = None

    def startup(self) -> None:
        pass

    def run(self) -> None:
        pass

    def shutdown(self) -> None:
        pass

    def support_rest_method(self):
        print("Testing RESTAPI specific method support for UIHandler scalability support.")