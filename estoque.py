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

estoque = {}


def adicionar_produto(produto, quantidade):
    estoque[produto] = quantidade
    return print(f"Produto {produto} adicionado com sucesso\n\n")


def remover_produto(produto):
    estoque.pop(produto)
    return print(f'Produto {produto} foi excluído com sucesso.\n\n')


def atualizar_quantidade(produto, nova_quantidade):
    estoque[produto] = nova_quantidade
    return print(f'A quantidade de {produto} foi atualizada para {nova_quantidade}.\n\n')


def exibir_estoque():
    if estoque:
        for produto, quantidade in estoque.items():
            print(f'Produto: {produto}, Quantidade: {quantidade}')
    else:
        print("O estoque está vazio.")
