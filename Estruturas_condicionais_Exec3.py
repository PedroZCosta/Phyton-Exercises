"""
Exercicio: Condição de pagamento
Criador: Pedro Henrique Zakrzevski Costa
Data: 22/03/2024
"""
# coletando informacoes com o usuario
print("O produto que voce escolheu custa R$35,50")
print("As formas de pagamento sao: ")
print("A vista em dinheiro ou cheque, recebe 10% de desconto")
print("A vista no cartão de crédito, recebe 15% de desconto")
print("Em duas vezes, preço normal de etiqueta sem juros")
print("Em tres vezes, preço normal de etiqueta mais juros de 10%")
payment = input("Por favor: digite sua forma de pagamento: ")
price = 35.50
final_price = 0
# calculo do preco do produto
if payment == "a vista em dinheiro" or payment == "a vista em cheque ":
    final_price = price * 0.9
elif payment == "a vista no cartao de credito" or payment == "a vista no cartao":
    final_price = price * 0.85
elif payment == "em tres vezes":
    final_price = price * 1.1
else:
    print("Opcao invalida")
print(f"Seu preco total foi de R${final_price: .2f}")
