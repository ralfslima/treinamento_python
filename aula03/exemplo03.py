# Variável número
numero = 0

# Variável contador
contador = 0

# Laço
while numero != -1:

    # Obter número e incrementar contador
    print('Informe um número ou -1 para finalizar')
    numero = int(input())
    contador += 1

    # Condicional para sair do laço
    if contador == 3:
        break