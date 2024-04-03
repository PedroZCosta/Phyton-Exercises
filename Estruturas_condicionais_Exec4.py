"""
Exercicio: destino do passageiro
Criador: Pedro Henrique Zakrzevski Costa
Data: 22/03/2024
versao: 1.0
"""
local_travel = input("Que regiao voce deseja viajar? (norte, nordeste, centro-oeste ou sul) ")
round_trip = input("Voce deseja fazer um  viagem de ida e volta? (s/n) ")
# precos fixos das viagens de ida
travel_price = 0
north = 500
northeast = 350
midwest = 350
south = 300
# precos adicionais da volta
north_back = 400
northeast_back = 300
midwest_back = 250
south_back = 250
# calculo do preco com a ida e a volta
if round_trip == "s" and local_travel == "norte":
    travel_price = north + north_back
elif round_trip == "s" and local_travel == "nordeste":
    travel_price = northeast + northeast_back
elif round_trip == "s" and local_travel == "centro_oeste":
    travel_price = midwest + midwest_back
elif round_trip == "s" and local_travel == "sul":
    travel_price = south + south_back
else:
    if local_travel == "norte":
        travel_price = north
    elif local_travel == "nordeste":
        travel_price = northeast
    elif local_travel == "centro-oeste":
        travel_price = midwest
    elif local_travel == "sul":
        travel_price = south
print(f"Sua passagem custa R${travel_price}")
