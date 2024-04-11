"""
Exercicio: Fazendo uso de laços, organizar e mostrar eles pedidos ao usuario em ordem crescente.
Criador: Pedro Henrique Zakrzevski Costa
Data: 09/04/2024
Versao: 1.0
"""

numbers = []
for i in range(5):
    num = int(input("Por favor, digite 5 numeros: "))
    numbers.append(num)
    numbers.sort()
print(numbers)
