"""
Exercicio: IMC – Índice de Massa Corporal
Criador: Pedro Henrique Zakrzevski Costa
Data: 29/03/2024
versao: 1.4
"""
# Faixas do IMC
range1 = 18.5
range2 = 25
range3 = 30
# Solicita as informacoes do usuario
peso = float(input("Digite seu peso? "))
alt = float(input("Digite sua altura em metros (exemplo: 1.83): "))
imc = (peso / (alt ** 2))
print(f"Seu resultado é:{imc: .1f}")
# Encontra onde o usuario se encontra na tabela do IMC
if imc < range1:
    print("Voce esta abaixo do peso!")
elif (imc >= range1) and (imc < range2):
    print("Voce tem um peso normal!")
elif (imc >= range2) and (imc < range3):
    print("Voce esta acima do peso!")
else:
    print("Voce tem obesidade!")
