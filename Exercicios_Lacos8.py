"""
Exercicio:
Criador: Pedro Henrique Zakrzevski Costa
Data: 11/04/2024
Versao: 1.0
"""
elevated_number = 0
final_sum = 0
num = input("Por favor, Digite um numero em binario para ser convertido em decimal (ex: 10110110): ")
while True:
    for bit in reversed(num):
        converted = int(bit) * (2 ** elevated_number)
        final_sum += converted
        elevated_number += 1
    #
    if elevated_number == len(num):
        break
    else:
        num = input("O número inserido não é binário. Por favor, insira um número binário válido: ")
        # Reinicializa as variáveis para recalcular a soma
        elevated_number = 0
        final_sum = 0
print(final_sum)
