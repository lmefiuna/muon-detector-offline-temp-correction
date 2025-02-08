from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str, params: tuple = None) -> None:
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: tuple = None) -> dict:
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: tuple = None) -> list[dict]:
        pass
