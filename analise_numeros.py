"""
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

"""
import statistics


def calcular_media(dados):
    return statistics.mean(dados)


def calcular_mediana(dados):
    return statistics.median(dados)


def calcular_desvio_padrao(dados):
    return statistics.stdev(dados)


def encontrar_maior(dados):
    return max(dados)


def encontrar_menor(dados):
    return min(dados)


def analisar_numeros():
    while True:
        entrada = input('Digite 10 números separados por espaço (ou "s" para sair): ')
        if entrada.lower() == 's':
            print("Saindo...")
            break
        dados = list(map(float, entrada.split()))

        if len(dados) != 10:
            print("Por favor, insira exatamente 10 números.")
            continue

        print(f"Média: {calcular_media(dados)}")
        print(f"Mediana: {calcular_mediana(dados)}")
        print(f"Desvio Padrão: {calcular_desvio_padrao(dados)}")
        print(f"Maior número: {encontrar_maior(dados)}")
        print(f"Menor número: {encontrar_menor(dados)}\n")


# Executar a análise de números
analisar_numeros()
