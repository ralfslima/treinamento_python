# 8ª O cliente informa dois valores inteiros.
# Se forem iguais, some os valores, caso contrário multiplique.

# Obter os valores
print('Informe um número')
numero1 = int(input())

print('Informe outro número')
numero2 = int(input())

# Verificação
resultado = str(numero1+numero2 if numero1 == numero2 else numero1 * numero2)

# Retorno
print(resultado)