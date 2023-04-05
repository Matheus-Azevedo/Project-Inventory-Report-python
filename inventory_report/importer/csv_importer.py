from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            inventory = [row for row in reader]
        return inventory
