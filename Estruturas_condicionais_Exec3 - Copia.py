print("O produto que voce escolheu custa R$ 35,50")
print("As formas de pagamento sao: ")
print("A vista em dinheiro ou cheque, recebe 10% de desconto")
print("A vista no cartão de crédito, recebe 15% de desconto")
print("Em duas vezes, preço normal de etiqueta sem juros")
print("Em tres vezes, preço normal de etiqueta mais juros de 10%")
payment = input("Por favor: digite sua forma de pagamento: ")
final_price = 35.50
if payment == "A vista em dinheiro" or payment == "A vista em cheque ":
    final_price * 0.9
    print(f"Seu preco total foi de R${final_price: .2f}")
elif payment == "A vista no cartao de credito" or payment == "A vista no cartao" :
    final_price * 0.85
    print(f"Seu preco total foi de R${final_price: .2f}")
elif payment == "Em duas vezes":
    print(f"Seu preco total foi de R${final_price: .2f}")
elif payment == "Em tres vezes":
    final_price* 1.1
    print(f"Seu preco total foi de R${final_price: .2f}")
else:
    print("Opcao invalida")
