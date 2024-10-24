"""
-----Gerenciamento de Estoque usando Dicionários e Módulos:

Crie um programa que gerencie um estoque de produtos. O estoque deve ser armazenado em um dicionário, onde
as chaves são os nomes dos produtos e os valores são suas quantidades.
O programa deve permitir adicionar novos produtos, remover produtos e atualizar a quantidade no estoque.
Implemente as seguintes funcionalidades usando funções:
adicionar_produto(produto, quantidade)
remover_produto(produto)
atualizar_quantidade(produto, nova_quantidade)
exibir_estoque()
Crie um módulo separado chamado estoque.py contendo essas funções, e importe-o no arquivo principal.
Dica: Utilize funções para manipular o dicionário e coleções para armazenar os dados do estoque.

Exemplo de saída:

yaml
Copiar código
1 - Adicionar Produto
2 - Remover Produto
3 - Atualizar Quantidade
4 - Exibir Estoque
0 - Sair

Escolha: 1
Digite o nome do produto: Arroz
Digite a quantidade: 50
Produto Arroz adicionado com sucesso!

Estoque atual:
Arroz: 50 unidades


"""
from estoque import adicionar_produto, remover_produto, atualizar_quantidade, exibir_estoque

opcao = ""
while opcao != "0":
    opcao = ""
    print("1 - Adicionar Produto \n2 - Remover Produto \n3 - Atualizar Quantidade \n4 - Exibir Estoque \n0 - Sair")
    opcao = input(f'Escolha: {opcao}')

    if opcao in ["1", "2", "3", "4"]:
        if opcao == "1":
            produto = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionar_produto(produto, quantidade)

        if opcao == "2":
            produto = input('Digite o nome do produto que deseja remover: ')
            remover_produto(produto)

        if opcao == "3":
            produto = input('Digite o nome do produto: ')
            nova_quantidade = int(input('Digite a nova quantidade quantidade: '))
            atualizar_quantidade(produto,nova_quantidade)

        if opcao == "4":
            exibir_estoque()

    elif opcao == "0":
            print('Saindo...')
