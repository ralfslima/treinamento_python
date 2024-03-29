# Informar dois números inteiros
# Retorne quantos são pares e quantos são ímpares

# Contadores
par = 0
impar = 0

# Obter o primeiro número
print('Informe um número')
numero1 = int(input())

# Obter o segundo número
print('Informe outro número')
numero2 = int(input())

# Laço
while numero1 <= numero2:
    
    # Condicional
    if numero1 % 2 == 0:
        par += 1
    else:
        impar += 1

    # Incrementar numero1
    numero1 += 1

# Exibir a quantidade de pares e ímpares
print('Pares: ' + str(par))
print('Ímpares: ' + str(impar))