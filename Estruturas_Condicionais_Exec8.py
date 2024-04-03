"""
Exercicio: Validacao de CPF
Criador: Pedro Henrique Zakrzevski Costa
Data: 03/04/2024
versao: 1.0
"""
# informacoes do usuario
cpf = input("Por favor, digite o seu CPF (Apenas numeros): ")
# Calculo das variaveis
calc = (int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 +
        int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2)
print(calc)
calc2 = (int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6
         + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2)
print(calc2)
# Calculo dos restos
rest = calc * 10 % 11
print(rest)
rest2 = calc2 * 10 % 11
print(rest2)
if rest == 10:
    rest = 0
# validando os digitos verificadores
if rest == int(cpf[9]) and rest2 == int(cpf[10]):
    print("Seu CPF e VALIDO!")
else:
    print("Seu CPF e INVALIDO!")
