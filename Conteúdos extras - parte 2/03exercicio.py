# 3ª Peça dois números e retorne quantos são pares e ímpares.

# Obter valores
print('Informe um número')
numero1 = int(input())

print('Informe outro número')
numero2 = int(input())

# Contadores
pares = 0
impares = 0

# Condicional para verificar qual é o menor número
if numero1 < numero2:
    # Laço de repetição
    while numero1 <= numero2:

        # Condicional
        if numero1 % 2 == 0:
            pares+=1
        else:
            impares+=1

        # Incremento
        numero1+=1
else:

    # Laço de repetição
    while numero1 >= numero2:

        # Condicional
        if numero1 % 2 == 0:
            pares+=1
        else:
            impares+=1

        # Incremento
        numero1-=1


# Exibir a quantidade de pares e ímpares
mensagem = 'Quantidade de pares: {}. Quantidade de ímpares {}.'
print(mensagem.format(str(pares), str(impares)))