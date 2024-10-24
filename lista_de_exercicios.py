"""
-----Calculadora com o Módulo math:

Crie um programa que peça ao usuário dois números e ofereça um menu de operações matemáticas (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Raiz Quadrada).
Implemente as operações usando o módulo math quando necessário, por exemplo, para calcular a raiz quadrada.
Utilize funções para cada operação e o loop while para permitir ao usuário realizar várias operações até que ele escolha sair.
Dica: Utilize estruturas condicionais (if/else) e loops (while) para manter o menu até que o usuário deseje sair.

Exemplo de saída:

makefile
Copiar código
Escolha uma operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Raiz Quadrada
0 - Sair

Escolha: 1
Digite o primeiro número: 8
Digite o segundo número: 4
Resultado: 12

-----Jogo de adivinhação com random:

Crie um programa que utilize o módulo random para gerar um número aleatório entre 1 e 100.
Peça ao usuário que adivinhe o número e forneça dicas como "Maior" ou "Menor" até que ele acerte.
Use loops para permitir que o jogo continue até que o usuário adivinhe corretamente.
No final, exiba quantas tentativas o usuário fez.
Dica: Utilize o loop while e operadores lógicos para verificar a condição de término.

Exemplo de saída:

mathematica
Copiar código
Tente adivinhar o número (entre 1 e 100): 50
O número é menor.
Tente adivinhar o número: 25
O número é maior.
Tente adivinhar o número: 32
Parabéns! Você acertou em 3 tentativas.


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


-----Análise de Números e Estatísticas:

Peça ao usuário que insira uma lista de 10 números inteiros.
Em seguida, utilize o módulo statistics (ou crie funções próprias) para calcular e exibir:
A média dos números.
A mediana.
O desvio padrão.
O maior e o menor número.
Implemente funções para cada cálculo e organize o programa em um loop para permitir diferentes entradas do usuário.
Dica: Se não usar o módulo statistics, implemente as fórmulas matemáticas para os cálculos de média, mediana e desvio padrão.

Exemplo de saída:

makefile
Copiar código
Digite 10 números separados por espaço: 10 20 30 40 50 60 70 80 90 100
Média: 55.0
Mediana: 55.0
Desvio Padrão: 28.722813232690143
Maior número: 100
Menor número: 10


-----Gerador de Senhas Aleatórias:

Crie um programa que gere uma senha aleatória de tamanho definido pelo usuário.
A senha deve conter letras maiúsculas, letras minúsculas, números e caracteres especiais.
Utilize o módulo random para gerar a senha, e a função join() para concatenar os caracteres gerados.
Permita que o usuário escolha quantas senhas ele quer gerar.
Dica: Use as funções random.choice() e random.sample() para selecionar caracteres de diferentes listas.

Exemplo de saída:

perl
Copiar código
Digite o tamanho da senha: 12
Quantas senhas você deseja gerar? 2
Senha 1: A1b@C9z#X4r!
Senha 2: m4T@c8K1lQ$s


-----Importando e Trabalhando com Módulos de Arquivos (os e csv):

Crie um programa que leia um arquivo CSV contendo uma lista de produtos e preços e exiba os dados de forma formatada.
Em seguida, o programa deve permitir adicionar novos produtos e salvar a atualização no arquivo CSV.
Utilize o módulo csv para manipular os arquivos e o módulo os para verificar se o arquivo já existe.
Dica: Use o módulo csv.reader() e csv.writer() para ler e escrever no arquivo CSV.

Exemplo de saída:

vbnet
Copiar código
Produto: Arroz, Preço: 10.50
Produto: Feijão, Preço: 7.00
Deseja adicionar um novo produto? (s/n): s
Digite o nome do produto: Macarrão
Digite o preço: 5.30
Produto adicionado com sucesso!
Esses exercícios integram as funcionalidades de módulos como math, random, csv, e os, enquanto consolidam os conhecimentos anteriores sobre variáveis, loops, estruturas condicionais, funções, e coleções. Isso permitirá que você desenvolva uma compreensão prática e integrada de como usar diversos recursos do Python.


"""