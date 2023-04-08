from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product('1',
                      'Arroz',
                      'Arroz da Trybe',
                      '2022-01-01',
                      '2023-01-01',
                      '123456789',
                      'em local seco')
    product_string = str(product)
    assert 'Arroz' in product_string
    assert 'Arroz da Trybe' in product_string
    assert '2022-01-01' in product_string
    assert '2023-01-01' in product_string
    assert 'em local seco' in product_string
