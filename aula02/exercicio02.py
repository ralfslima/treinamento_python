# 2ª Peça dois números, se forem iguais realize 
# a soma deles, caso contrário realize a multiplicação.

# Obter números
print('Informe o primeiro número')
numero1 = int(input())

print('Informe o segundo número')
numero2 = int(input())
      
# Cálculos
#if numero1 == numero2:
#    print('A soma dos valores é ' + str(numero1+numero2))
#else:
#    print('A multiplicação dos valores é ' + str(numero1*numero2))

# Operador ternário
# Exemplo PHP/JAVA/C#: numero1 == numero2 ? numero1+numero2 : numero1*numero2
calculo = numero1 + numero2 if numero1 == numero2 else numero1 * numero2
print(str(calculo))