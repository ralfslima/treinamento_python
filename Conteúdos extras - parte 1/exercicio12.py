# 12ª Peça um verbo terminado em AR e realize sua conjugação.

# Obter o verbo terminado em ar
print('Informe um verbo terminado em AR')
verbo = input()

# Extrair
parte1 = verbo[0:len(verbo)-2]
parte2 = verbo[len(verbo)-2] + verbo[len(verbo)-1]

# Condicional
if parte2 != 'ar':
    print('Não é um verbo terminado em AR')
else:
    print('Eu ' + parte1 + 'o')
    print('Tu ' + parte1 + 'as')
    print('Ele ' + parte1 + 'a')
    print('Nós ' + parte1 + 'amos')
    print('Vós ' + parte1 + 'ais')
    print('Eles ' + parte1 + 'am')