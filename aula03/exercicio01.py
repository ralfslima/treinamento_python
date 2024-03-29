# O cliente informa um número, em seguida
# retorne a tabuada daquele valor

# Obter o valor para realizar a tabuada
print('Informe um número para realizar a tabuada')
numero = int(input())

# Índice
indice = 1

# Laço
while indice < 11:
    print(str(numero) + ' X ' + str(indice) + ' = ' + str(numero*indice))
    indice += 1