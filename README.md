# Inventory Report
### Autor: Matheus Eduardo de Sousa Azevedo

Este projeto foi desenvolvido por mim e faz parte do acervo de atividades executadas na escola de programação Trybe. A formação ao longo de 1 ano em Desenvolvimento Web desta instituição  conta com mais de 1.500 horas de aulas e aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais. Tudo voltado totalmente para o mercado de trabalho com intuito de entregar um profissional adequado para a realidade atual. 

# Sobre o projeto

O projeto consiste na implementação de um gerador de relatórios orientado a objetos em Python que lê dados de estoque de arquivos CSV, JSON ou XML e gera um relatório simples ou completo. As habilidades trabalhadas incluem conceitos de orientação a objetos, padrões de projeto e leitura/escrita de arquivos em diferentes formatos. O objetivo é aplicar conhecimentos em programação e estruturação de dados para gerar relatórios eficientes e precisos a partir de fontes diversas.

# O que foi desenvolvido

Funcionalidade 1: Testar o construtor/inicializador do objeto Produto.

-   Implementar testes para o método init da classe Product.
-   Garantir que o método está preenchendo corretamente os atributos.

Funcionalidade 2: Gerar a versão simplificada do relatório.

-   Implementar um método para gerar um relatório contendo as seguintes informações:
    -   Data de fabricação mais antiga.
    -   Data de validade mais próxima.
    -   Empresa com mais produtos.

Funcionalidade 3: Gerar a versão completa do relatório.

-   Implementar um método para gerar um relatório contendo as seguintes informações:
    -   Data de fabricação mais antiga.
    -   Data de validade mais próxima.
    -   Empresa com mais produtos.
    -   Quantidade de produtos estocados por empresa.

Funcionalidade 4: Gerar os relatórios através de um arquivo CSV.

-   Implementar um método import_data que recebe um arquivo CSV e chama o método de geração de relatório correspondente.
-   O tipo de relatório é especificado como parâmetro.

Funcionalidade 5: Gerar os relatórios através de um arquivo JSON.

-   Implementar um método import_data que recebe um arquivo JSON e chama o método de geração de relatório correspondente.
-   O tipo de relatório é especificado como parâmetro.
