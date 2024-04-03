'''
Exercicio: Calculo de peso ideal
Criador: Pedro Henrique Zakrzevski Costa
Data: 03/04/2024
versao: 1.0
'''
sex = input("Por favor, digite seu sexo (h/m): ")
height = float(input("Por favor, digite sua altura em metros (Exemplo: 1.86): "))
if sex == "h":
    calc = 72.7 * height - 58
else:
    calc = 62.1 * height - 44.7
print(f"O seu peso ideal e:{calc: .1f}")