from abc import ABC, abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass


class OtherSubClient(BaseClient):
    def connect(self):
        pass

    def close(self):
        pass

    def retrieve(self):
        pass
