"""
Verificar se a palavra e um palindromo
"""
inverse_word = ""
word = input("Por favor, digite uma palavra para verificar se e um palindromo? ")
for letter in word:
    # a ordem da soma de uma str importa, ela sem inverter adicionaria os numeros na forma normal
    inverse_word = letter + inverse_word
if inverse_word == word:
    print(f"A palavra {inverse_word} e um palindromo")
else:
    print(f"A palavra {inverse_word} nao e um palindromo")
