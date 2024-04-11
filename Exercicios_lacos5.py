"""
Exercicio:  calcular e imprimir o tempo necessário para que a população do país A ultrapasse a população do país B
Criador: Pedro Henrique Zakrzevski Costa
Data: 10/04/2024
Versao: 1.0
"""
years = 0
population_a = 5000000
population_b = 7000000
birth_rate_a = 0.03
birth_rate_b = 0.02
while population_a <= population_b:
        population_a += population_a * birth_rate_a
        population_b += population_b * birth_rate_b
        years += 1
print("Tempo necessário para que a população do país A ultrapasse a população do país B:", years, "anos.")
