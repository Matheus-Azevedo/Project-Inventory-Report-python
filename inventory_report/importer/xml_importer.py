from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()
        inventory = []
        for child in root:
            product = {}
            for subchild in child:
                product[subchild.tag] = subchild.text
            inventory.append(product)
        return inventory
