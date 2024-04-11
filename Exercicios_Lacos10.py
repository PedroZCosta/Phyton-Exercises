"""
Exercicio:
Criador: Pedro Henrique Zakrzevski Costa
Data: 11/04/2024
Versao: 1.0
"""
"""
Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos).
"""
from datetime import datetime,timedelta
date1 = input("digite a data inicial (no formato dd/mm/YYYY): ")
date2 = input("digite a data final para saber o intervalo (dd/mm/YYYY): ")
data1 = datetime.strptime(date1, "%d/%m/%Y")
data2 = datetime.strptime(date2, "%d/%m/%Y")
quantity = (data2 - data1)
print("a quantidade é de",quantity)

