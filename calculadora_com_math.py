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



 -- Como ficou o resultado --

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
O resultado da soma é: 12.0
"""
from math import sqrt

opcao = ""
while opcao != "0":
    opcao = ""
    print(
        'Escolha uma operação: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Raiz Quadrada \n0 - Sair\n')
    opcao = input(f'Escolha: {opcao}')

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if opcao == "1":
            res = num1 + num2
            print(f'O resultado da soma é: {res}\n\n')

        elif opcao == "2":
            res = num1 - num2
            print(f'O resultado da subtração é: {res}\n\n')

        elif opcao == "3":
            res = num1 * num2
            print(f'O resultado da multiplicação é: {res}\n\n')

        elif opcao == "4":
            if num2 != 0:
                res = num1 / num2
                print(f'O resultado da divisão é: {res}\n\n')
            else:
                print('Não é possível fazer divisão por zero \n\n')

    elif opcao == "5":
        num = float(input('Digite o número para calcular a raiz quadrada: '))
        if num >= 0:
            res = sqrt(num)
            print(f'O resultado da raiz quadrada desse número é {res}\n\n')
        else:
            print('Não é possível calcular a raiz quadrada desse número.\n\n')

    elif opcao == "0":
        print('Saindo...')

    else:
        print('Opção inválida. Tente novamente.\n\n')


class Calculadora:
    def soma(self,num1,num2):
        return num1 + num2

    def subtracao(self,num1,num2):
        return num1 - num2

calc = Calculadora()
calc.soma(1,2)