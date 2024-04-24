# 9ª Peça o tamanho dos quatro lados de uma caixa.
# Se os lados foram iguais, retorne que é uma caixa quadrada.
# Caso contrário, retorne que não é uma caixa quadrada.

# Obter os quatro lados
print('Informe o primeiro lado')
lado1 = int(input())

print('Informe o segundo lado')
lado2 = int(input())

print('Informe o terceiro lado')
lado3 = int(input())

print('Informe o quarto lado')
lado4 = int(input())

# Condicional
if lado1 == lado2 and lado2 == lado3 and lado3 == lado4:
    print('É uma caixa quadrada')
else:
    print('Não é uma caixa quadrada')