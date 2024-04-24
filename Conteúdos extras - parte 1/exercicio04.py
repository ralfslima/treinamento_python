# 4ª Informe o valor de um produto e a forma de pagamento (a vista ou a prazo).
# Caso o valor seja superior a R$1000,00 e à vista, teremos um desconto de 20%
# Caso o valor seja superior a R$500,00 e à vista, teremos um desconto de 10%
# Caso contrário não haverá desconto.

# Obter o valor do produto
print('Informe o valor do produto')
valor = float(input())

# Obter a forma de pagamento
print('Escolha a forma de pagamento')
print('1) À vista')
print('2) A prazo')
pagamento = int(input())

# Condicional
if valor > 1000 and pagamento == 1:
    msg = 'Desconto de 20%! Total a pagar R${}'
    print(msg.format(str(valor*0.8)))
elif valor > 500 and pagamento == 1:
    msg = 'Desconto de 10%! Total a pagar R${}'
    print(msg.format(str(valor*0.9)))
else:
    msg = 'Não haverá desconto! Total a pagar R${}'
    print(msg.format(str(valor)))