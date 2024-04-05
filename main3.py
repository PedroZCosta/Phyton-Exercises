'''
validar float com . e ,
'''
while True:
    num_str = input("Por favor, digite o valor do seu salario com 2 casas decimais: ")
    subst = ""
    ##
    for i in num_str:
        if i == ",":
            subst += "."
        else:
            subst += i
    ##
    try:
        num = float(subst)
        break
    except:
        print("Dados invalidos. Favor tentar novamente")
print((subst))

# maneira mais facil de substituir
# num_str.raplace(",", ".")