# 3ª Peça um número, retorne se é um 
# número positivo ou negativo.

# Tentativa
try:

    # Obter número
    print('Informe um número')
    numero = int(input())

    # Retorno
    print('Positivo' if numero >= 0 else 'Negativo')

except:

    # Retorno caso o cliente informe uma letra
    print('Informe apenas números inteiros')