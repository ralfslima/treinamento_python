# 1ª Pedir um número e retornar a tabuada do valor informado.

# Obter o número
print('Informe um número')
numero = int(input())

# Laço
indice = 0
while indice < 11:
    print(str(numero) + ' X ' + str(indice) + ' = ' + str(numero*indice))
    indice+=1