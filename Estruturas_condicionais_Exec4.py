local_travel = input("Que regiao voce deseja viajar? (norte, nordeste, centro-oeste ou sul) ")
round_trip = input("Voce deseja fazer um  viagem de ida e volta? (s/n) ")
# precos fixos das viagens de ida
travel_price = 0
north = 500
northeast = 350
midwest = 350
south = 300
# calculo do preco com a ida e a volta
if round_trip == "s" and local_travel == "norte":
    travel_price = north + 400
elif round_trip == "s" and local_travel == "nordeste":
    travel_price = northeast + 300
elif round_trip == "s" and local_travel == "centro_oeste":
    travel_price = midwest + 250
elif round_trip == "s" and local_travel == "sul":
    travel_price = south + 250
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