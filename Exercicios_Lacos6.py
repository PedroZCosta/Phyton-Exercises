"""
Exercicio:
Criador: Pedro Henrique Zakrzevski Costa
Data: 11/04/2024
Versao: 1.0
"""
first_name = ""
last_name = ""
certo = ""
name = input("Por favor, digite o seu nome inteiro: ")
# se tiver vazio para e adiciona os elem em algum acumulador para o primeiro nome
for f in name:
    if f == " ":
        break
    else:
        first_name += f
for f in reversed(name):
    # se tiver vazio para e adiciona os elem em algum acumulador para o segundo nome
    if f == " ":
        break
    else:
         last_name += f
# inverte o ultimo nome para ficar certo
for f in last_name:
        f = last_name
for i in f:
    certo = i + certo
print(f"O seu primeiro nome e {first_name} e o seu ultimo nome e {certo}")
