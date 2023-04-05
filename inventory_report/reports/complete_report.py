from inventory_report.reports.simple_report import SimpleReport
from collections import OrderedDict


class CompleteReport(SimpleReport):
    def __init__(self, inventory: list[dict]):
        super().__init__(inventory)

    @staticmethod
    def qtt_by_company(inventory: list[dict]) -> str:
        companies = OrderedDict()
        for product in inventory:
            companies[product["nome_da_empresa"]] = companies.get(
                product["nome_da_empresa"], 0) + 1
        return "Produtos estocados por empresa:\n" + \
               "".join(f"- {company}: {qtt}\n"
                       for company, qtt in companies.items())

    @staticmethod
    def generate(inventory) -> dict:
        simple_report = SimpleReport.generate(inventory)
        companies = CompleteReport.qtt_by_company(
            inventory)
        return f"{simple_report}\n" \
               f"{companies}"
