'''
Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!".
'''
while True:
        login = input("Por favor, digite o seu login: ")
        password = input("Por favor, digite a sua senha: ")
        try:
            if login != password:
                print("Seja bem vindo ao sistema!!!")
                break
            else:
                print("Dados invalidos.")
        except:
            print("Dados invalidos. Favor tentar novamente")
