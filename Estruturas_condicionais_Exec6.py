# Informacoes do usuario
user_day = int(input("Por favor, digite seu dia de nascimento: "))
user_month = int(input("Por favor, digite seu mes de nascimento (Em extenso): "))
user_year = int(input("Por favor, digite seu dia de nascimento (Com 4 digitos): "))
date_display = input("Voce deseja que a data seja exibida de maneira simples, abreviada ou completa? ")
# conversao de meses em nome para numero
janeiro = "01"
fevereiro = "02"
marco = "03"
abril = "04"
maio = "05"
junho = "06"
julho = "06"
agosto = "08"
setembro = "09"
outubro = "10"
novembro = "11"
dezembro = "12"
# resolucao da forma de exibicao da data
if date_display == "simples":
    print(f"{user_day}/{user_month}/{user_year}")
elif date_display == "abreviada":
    print(f"{user_day}/{user_month}/{user_year}")
else:
    print(f"{user_day}/{user_month}/{user_year}")
