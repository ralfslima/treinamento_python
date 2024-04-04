# Peça uma palavra, em seguida retorna a palavra,
# intercalando entre maiúsculas e minúsculas
# Exemplo: bola -> BoLa, Python -> PyThOn

# Obter uma palavra
print('Informe uma palavra')
palavra = input()

# Laço de repetição
indice = 0
while indice < palavra.count('')-1:
    
    if indice % 2 == 0:
        print(palavra[indice].upper())
    else:
        print(palavra[indice].lower())

    indice+=1