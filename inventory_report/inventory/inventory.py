import os.path
import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def import_data(file_path: str, type: str) -> list[dict]:
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == ".csv":
            inventory = Inventory.import_csv(file_path)
        elif file_extension == ".json":
            inventory = Inventory.import_json(file_path)
        elif file_extension == ".xml":
            inventory = Inventory.import_xml(file_path)
        else:
            raise ValueError("Arquivo inválido")
        return Inventory.generate_report(inventory, type)

    @staticmethod
    def import_csv(path: str) -> list[dict]:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def import_json(path: str) -> list[dict]:
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def import_xml(path: str) -> list[dict]:
        tree = ET.parse(path)
        root = tree.getroot()
        inventory = []
        for child in root:
            product = {}
            for subchild in child:
                product[subchild.tag] = subchild.text
            inventory.append(product)
        return inventory

    @staticmethod
    def generate_report(inventory: list[dict], type: str) -> str:
        if type == "simples":
            return SimpleReport.generate(inventory)
        elif type == "completo":
            return CompleteReport.generate(inventory)
        else:
            raise ValueError("Tipo inválido")
