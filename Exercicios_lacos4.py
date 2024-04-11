"""
Exercicio: Fazendo uso de laços, organizar e mostrar eles pedidos ao usuario em ordem crescente.
Criador: Pedro Henrique Zakrzevski Costa
Data: 09/04/2024
Versao: 1.0
"""
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
num3 = float(input("digite o terceiro numero: "))
num4 = float(input("digite o quarto numero: "))
num5 = float(input("digite o quinto numero: "))
while True:
    if num1 < num2 <num3 <num4 < num5:
        break
    elif num1 > num2:
        x = num1
        num1 = num2
        num2 = x
    elif num2 > num3:
        x = num2
        num2 = num3
        num3 =x
    elif num3 > num4:
        x = num3
        num3 = num4
        num4 = x
    elif num4 > num5:
        x = num4
        num4 = num5
        num5 = x
print(f"{num1},{num2},{num3},{num4},{num5}")
