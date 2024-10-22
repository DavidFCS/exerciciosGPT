"""
-----Calculadora com o Módulo math:

Crie um programa que peça ao usuário dois números e ofereça um menu de operações matemáticas
 (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Raiz Quadrada).
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

"""
import math

opcao = ""

while opcao != "0":
      opcao = input(print('Escolha uma operação: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Raiz Quadrada \n0 - Sair\n'))
      print(f'Escolha: {opcao}')


      if opcao == "1":
