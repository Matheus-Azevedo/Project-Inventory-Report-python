from datetime import datetime


class SimpleReport:
    def __init__(self, inventory: list[dict]):
        self.inventory = inventory

    @staticmethod
    def oldest_manufacturing_date(inventory: list[dict]) -> str:
        oldest_manufacturing_date = min(
            product["data_de_fabricacao"] for product in inventory
        )
        return f"Data de fabricação mais antiga: {oldest_manufacturing_date}"

    @staticmethod
    def closest_expiration_date(inventory: list[dict]) -> str:
        today = datetime.today().strftime("%Y-%m-%d")
        closest_expiration_date = min(
            product["data_de_validade"] for product in inventory if
            product["data_de_validade"] > today
        )
        return f"Data de validade mais próxima: {closest_expiration_date}"

    @staticmethod
    def company_with_more_products(inventory: list[dict]) -> str:
        companies = {}
        for product in inventory:
            companies[product["nome_da_empresa"]] = companies.get(
                product["nome_da_empresa"], 0) + 1
        company_with_more_products = max(companies, key=companies.get)
        return f"Empresa com mais produtos: {company_with_more_products}"

    @staticmethod
    def generate(inventory: list[dict]) -> dict:
        manufacturing_date = SimpleReport.oldest_manufacturing_date(inventory)
        expiration_date = SimpleReport.closest_expiration_date(inventory)
        company = SimpleReport.company_with_more_products(inventory)

        return f"Data de fabricação mais antiga: {manufacturing_date}\n" \
               f"Data de validade mais próxima: {expiration_date}\n" \
               f"Empresa com mais produtos: {company}\n"
