"""
Exercicio: jogo de par ou ímpar
Criador: Pedro Henrique Zakrzevski Costa
Data: 22/03/2024
versao: 1.3
"""
# solicitar ao usuario a escolha de par ou impar
jog1 = input("Jogador 1, voce deseja ser par ou impar? ")
if jog1 == "par":
    print("Jogador 1 sera par e Jogador 2 sera impar")
else:
    print("Jogador 1 sera impar e Jogador 2 sera par")
# solicitar aos usuarios valores
num1 = int(input("Escolha um numero de 1 a 5: "))
num2 = int(input(f"Escolha um numero de 1 a 5: "))
soma = num1 + num2
# verifica se a soma dos numeros se enquadra em par ou impar
if soma % 2 == 0:
    if jog1 == "par":
        print("Jogador 1 ganhou")
    else:
        print("Jogador 2 ganhou")
else:
    if j1 == "impar":
        print("Jogador 1 ganhou")
    else:
        print("Jogador 2 ganhou")