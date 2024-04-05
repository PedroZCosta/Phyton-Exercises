'''
Criar um programa que gera a série de Fibonacci até enquanto o valor for menor que um valor informado pelo usuário.
Obs.: Série de Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1  e
partir deste ponto sempre será a soma dos dois valores anteriores.
'''
fib = [0, 1]
while True:
    try:
        fvalue = int(input("Por favor digite o valor limite que deseja para a sequencia de Fibonacci: "))
        break
    except:
        print("Valor invalido!!!")
while fib[-1] <= fvalue:
    soma_acumulada = (fib[-1] + fib[-2])
    if soma_acumulada <= fvalue:
        fib.append(soma_acumulada)
    else:
        break
print(fib)



