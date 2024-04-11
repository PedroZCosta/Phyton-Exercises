"""
Exercicio: Jogo de pedra, papel, tesoura entre dois jogadores
Criador: Pedro Henrique Zakrzevski Costa
Data: 06/04/2024
Versao: 1.0
"""
counter_jog1 = 0
counter_jog2 = 0
play_counter = 0
win_points = 0
while True:
    try:
        win_points = int(input("Por favor, digite a quantidade de pontos a serem feitos para vencer: "))
        if win_points < 0:
            print("Este valor nao pode ser negativo, por favor tente novamente.")
        if win_points == 0:
            print("Este valor nao pode ser 0, por favor tente novamente.")
            break
    except ValueError:
        print("Valor invalido. Por favor tente novamente!!!")
    while True:
        if counter_jog1 == win_points or counter_jog2 == win_points:
            if counter_jog1 > counter_jog2:
                print("O jogador 1 ganhou o jogo!!!")
                break
            else:
                print("O jogador 2 ganhou o jogo!!!")
                break
        else:
            play_counter += 1
            jog1 = input(f"Jogador 1 digite sua {play_counter}° jogada (pedra, papel ou tesoura): ")
            jog2 = input(f"Jogador 2 digite sua {play_counter}° jogada (pedra, papel ou tesoura): ")
            for i in jog1:
                if jog1 not in ["pedra", "papel", "tesoura"]:
                    print("Jogador 1 digitou sua escolha errada, comece novamente!")
                    break
            for i in jog2:
                if jog2 not in ["pedra", "papel", "tesoura"]:
                    print("Jogador 2 digitou sua escolha errada, comece novamente!")
                    break
        # Todas possibilidades do jogo
            if jog1 == "pedra":
                if jog2 == "pedra":
                    print(f"A {play_counter}° rodada empatou")
                elif jog2 == "papel":
                    print(f"O jogador 2 ganhou a rodada {play_counter}°")
                    counter_jog2 += 1
                else:
                    print(f"O jogador 1 ganhou a rodada {play_counter}°")
                    counter_jog1 += 1
            elif jog1 == "papel":
                if jog2 == "pedra":
                    print(f"O jogador 1 ganhou a rodada {play_counter}°")
                    counter_jog1 += 1
                elif jog2 == "papel":
                    print(f"A {play_counter}° rodada empatou")
                else:
                    print(f"O jogador 2 ganhou a rodada {play_counter}°")
                    counter_jog2 += 1
            elif jog1 == "tesoura":
                if jog2 == "pedra":
                    print(f"O jogador 2 ganhou a rodada {play_counter}°")
                    counter_jog2 += 1
                elif jog2 == "papel":
                    print(f"O jogador 1 ganhou a rodada {play_counter}°")
                    counter_jog1 += 1
                else:
                    print(f"A {play_counter}° rodada empatou")
