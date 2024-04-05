'''
Criar um programa que simula um carrinho de compras, onde
solicita o nome do produto (não pode ser vazio), o valor deste
produto (valor com vírgula, positivo) e a quantidade deste
produto a ser comprada (valor inteiro, positivo). Ao incluir um
produto, deve perguntar se o usuário deseja fechar o pedido ou
incluir mais produtos. Todos os dados devem ser validados. Ao
final da compra, deve ser informado o valor total do pedido.
'''
while True:
    prod_name = input("Por favor, digite o nome do produto: ")
    prod_value =