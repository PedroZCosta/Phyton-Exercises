import math
# verifica as informacoes do usuario
var1 = int(input("Digite o numero que voce deseja calcular A: "))
var2 = int(input("Digite o numero que voce deseja calcular B: "))
var3 = int(input("Digite o numero que voce deseja calcular C: "))
delta = (var2 ** 2 - 4 * var1 * var3)
raiz_delta = 0
# verifica se o valor dentro da raiz quadrada nao e negativo
if delta >= 0:
    raiz_delta = math.sqrt(delta)
else:
    print("Delta e negativo, nao e possível calcular a raiz quadrada.")
# Calcula os valores de x1 e x2
x1 = (-var2 + raiz_delta) / (2 * var1)
x2 = (-var2 - raiz_delta) / (2 * var1)
print(f"Seu valor de x1: {x1} e seu valor de x2: {x2}")
