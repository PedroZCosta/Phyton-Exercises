"""
Exercicio: Código de Exibição de Data
Criador: Pedro Henrique Zakrzevski Costa
Data: 30/03/2024
versao: 1.6
"""
# Informacoes do usuario
user_day = int(input("Por favor, digite seu dia de nascimento: "))
user_month = input("Por favor, digite seu mes de nascimento (Em extenso): ")
user_year = int(input("Por favor, digite seu dia de nascimento (Com 4 digitos): "))
date_display = input("Voce deseja que a data seja exibida de maneira simples, abreviada ou completa? ")
# resolucao da forma de exibicao da data
if date_display == "simples":
    # Dicionario de meses em exibicao simples
    number_months = {
        "janeiro": "01",
        "fevereiro": "02",
        "marco": "03",
        "abril": "04",
        "maio": "05",
        "junho": "06",
        "julho": "07",
        "agosto": "08",
        "setembro": "09",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }
    if user_month.lower() in number_months:
        user_month = number_months[user_month.lower()]
    print(f"{user_day}/{user_month}/{user_year}")
# Data abreviada
elif date_display == "abreviada":
    abbreviated_months = user_month[:3]
    print(f"{user_day}/{abbreviated_months}/{user_year}")
else:
    print(f"{user_day}/{user_month}/{user_year}")
