from .SubClient import SubClient


class Client:
    def __init__(self):
        ## implement factory if pattern for further various subclients
        self.client = SubClient

    def connect(self, *args):
        self.client.connect(*args)

    def close(self):
        self.client.close()

    def retieve(self, *args):
        self.client.retrieve(*args)

