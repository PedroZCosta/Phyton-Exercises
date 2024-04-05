'''
Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados
'''
num_counter = 0
sum = 0
media = 0
while True:
    num = int(input("Por favor digite um numero (0 para parar): "))
    sum += num
    num_counter += 1
    try:
        if num == 0:
            break
        if num < 0:
                continue
        if num_counter > 0:
            media = sum / num_counter
    except:
            print("erro")
print(media)

