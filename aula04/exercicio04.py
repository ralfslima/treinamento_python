# Pedir 5 números inteiros, em seguida exibir
# os valores.
# Não poderá haver números iguais

# Lista de números
numeros = []

# Contador (Para saber quantos números diferentes temos armazenados)
contador = 0

# Laço While
while contador < 5:

    # Obter um número
    print('Informe o '+str(contador+1)+'º número')
    numero = int(input())

    # Variável para verificar se existe o número na lista
    existe = 0

    # Laço de repetição
    for n in numeros:
        if n == numero:
            existe = 1
            break
    
    # Caso o número não exista
    if existe == 0:
        contador += 1
        numeros.append(numero)
    else:
        print('O número '+str(numero)+' já foi informado!')

# Exibir os valores sem repetição
for n in numeros:
    print(n)