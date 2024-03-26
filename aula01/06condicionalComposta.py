# Obter o valor da compra
print('Informe o valor da compra')
valor = float(input())

# Obter a forma de pagamento
print('Informe a forma de pagamento')
print('1º Dinheiro ou Pix')
print('2º Cartão de crédito ou débito')
pagamento = int(input())

# Condicional - Se o valor da compra for de pelo menos R$100,00
# e a forma de pagamento for Dinheiro ou Pix, daremos 10% de desconto
if valor >= 100 and pagamento == 1:
    print('Total a pagar com desconto R$ ' + str(valor * 0.9))
else:
    print('Total a pagar R$ ' + str(valor))

# AND -> E
# OR  -> OU