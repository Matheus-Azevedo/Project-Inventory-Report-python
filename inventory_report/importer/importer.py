from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, path: str, type: str) -> list[dict]:
        raise NotImplementedError
