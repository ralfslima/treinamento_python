# Faça uma tabuada, utilizando o laço FOR

# Obter o valor para realizar a tabuada
print('Informe um número para realizar a tabuada')
numero = int(input())

# Laço FOR
for n in range(1, 11):
    print(str(numero) + ' X ' + str(n) + ' = ' + str(numero*n))