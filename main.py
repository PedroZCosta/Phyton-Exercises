'''
efetuar a soma de numeros dados pelo usuario (0 para parar)
'''
# Acumulador
soma = 0
# pode ser qualquer numero pois ele sera substituido pelo primeiro "laço"!
num = -1
while True:
    num = int(input("Por favor, digite um numero positivo para somar (0 para sair): "))
    # aqui ele sai do loop
    if num == 0:
        break
    # ele verifica se o numero nao e negativo
    if num < 0:
        continue
    soma += num
print(f"A soma dos numeros é {soma}")
