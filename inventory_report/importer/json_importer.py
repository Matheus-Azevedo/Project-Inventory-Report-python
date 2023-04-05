from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            inventory = json.load(file)
        return inventory
