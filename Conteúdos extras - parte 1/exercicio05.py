# 5ª O cliente informe o ano, retorne se é bissexto ou não.

# Pedir o ano
print('Informe um ano.')
ano = int(input())

# Verificação
#if ano % 4 == 0:
#    print('É um ano bissexto')
#else:
#    print('Não é um ano bissexto')

print('Bissexto' if ano % 4 == 0 else 'Não é bissexto')