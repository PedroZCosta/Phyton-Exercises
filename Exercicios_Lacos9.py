"""
Exercicio:
Criador: Pedro Henrique Zakrzevski Costa
Data: 11/04/2024
Versao: 1.0
"""
"""
Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas.
"""
resto = 1
right = ""
f_right = ""
quociente = 0
continue_q = 1
while True:
    num = int(input("Por favor, digite o numero decimal: "))
    resto = num % 16
    quociente = num // 16
    # enquanto o quociente nao chegar a 0 ele continuara dividindo
    while quociente != 0:
        if quociente < 16:
            resto = quociente
        resto = quociente % 16
        quociente = quociente // 16
        # Se o rest0 dor maior que 10 ele converte os numeros depois do 10 em simbolos hexadecimas
        if resto < 10:
            f_right = str(resto) + right
        if resto == 10:
            f_right = "A" + right
        if resto == 11:
            f_right = "B" + right
        if resto == 12:
            f_right = "C" + right
        if resto == 13:
            f_right = "D" + right
        if resto == 14:
            f_right = "E" + right
        if resto == 15:
            f_right = "F" + right
    if continue_q == 0 or quociente == 0:
        break
print(f_right)
