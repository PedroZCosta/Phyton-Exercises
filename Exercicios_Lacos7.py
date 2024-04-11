"""
Exercicio:
Criador: Pedro Henrique Zakrzevski Costa
Data: 11/04/2024
Versao: 1.0
"""
a_counter = 0
while True:
    word = input("Por favor, digite uma palavra (nao digite nada para parar): ")
    for i in word:
        if i == "a" or i == "A":
            a_counter += 1
    if word == "":
        break
print(a_counter)
