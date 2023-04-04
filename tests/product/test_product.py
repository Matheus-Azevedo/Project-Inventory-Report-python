from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Café",
        "Nescafé",
        "2020-01-01",
        "2020-12-31",
        "123456789",
        "Em local seco e arejado",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Café"
    assert product.nome_da_empresa == "Nescafé"
    assert product.data_de_fabricacao == "2020-01-01"
    assert product.data_de_validade == "2020-12-31"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "Em local seco e arejado"
