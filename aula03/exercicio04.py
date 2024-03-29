# Random (Informações aleatórias)

# Importar o randomrange
from random import randrange

# Teste - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
aleatorio = (randrange(10) + 1)

# Exibir o valor gerado
print('Valor gerado -> ' + str(aleatorio))

# Crie um laço de repetição, onde o cliente informa um número entre 1 e 10
# Enquanto o cliente não informar o número que foi gerado, estará no laço
# Quando acertar o número, informe quantas vezes errou

# Criar uma variável para armazenar um número
numero = 0

# Contador de erros
erros = 0

# Laço
while numero != aleatorio:
    print('Informe um número entre 1 e 10')
    numero = int(input())

    if numero == aleatorio:
        break
    else:
        erros += 1

# Exibir a quantidade de erros
print('Você errou ' + str(erros) + ' vez(es)')