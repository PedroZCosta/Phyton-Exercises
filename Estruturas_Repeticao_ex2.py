'''
Solicitar ao usuario e validar a entrada de dados (um numero de 1 a 5)
'''
while True:
    name = input("Digite o seu nome: ")
    if name != "":
            break
while True:
    try:
        num = int(input("Digite um numero de 1 a 5: "))
        if 1 <= num <= 5:
            break
    except:
        print("Dados invalidos. Favor tentar novamente")
