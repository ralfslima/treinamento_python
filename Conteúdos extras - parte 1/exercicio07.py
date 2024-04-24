# 7ª Peça três números e retorne o maior deles

# Obter os três números
print('Informe o primeiro número')
numero1 = int(input())

print('Informe o segundo número')
numero2 = int(input())

print('Informe o terceiro número')
numero3 = int(input())

# Maior número
maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

# Retorno
print('O maior número é ' + str(maior))