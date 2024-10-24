"""
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
"""

import random

letras_maisculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_munusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres_especiais = "!@#$%^&*()-_=+<>?"

