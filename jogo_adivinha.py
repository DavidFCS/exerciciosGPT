"""
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

"""
import random

tentativas = 0
num = random.randint(1,101)

jogada = int(input('Tente adivinhar o número (entre q e 100): '))

while jogada != num:
    if jogada > num:
        tentativas =  tentativas + 1
        print('O número é menor.')
        jogada = int(input('Tente adivinhar o número: '))

    elif jogada < num:
        print('O número é maior.')
        jogada = int(input('Tente adivinhar o número: '))

else:
    tentativas = tentativas + 1
    print(f'Parabens! Você acertou em {tentativas} tentativas')
