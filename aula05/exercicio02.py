# Conjugar um verbo terminado em AR.
# Valide caso não termine em AR.
# Exemplo: andar
# Eu ando
# Tu andas
# Ele anda
# Nós andamos
# Vós andais
# Eles andam 

# Palavra
palavra = 'fabricar'

# Início da palavra
inicio = palavra[0:palavra.count('')-3]

# Final da palavra
final = palavra[palavra.count('')-3] + palavra[palavra.count('')-2]

# Condicional
if final != 'ar':
    print('Não é um verbo terminado em AR')
else:
    print('Eu '+inicio+'o')
    print('Tu '+inicio+'as')
    print('Ele '+inicio+'a')
    print('Nós '+inicio+'amos')
    print('Vós '+inicio+'ais')
    print('Eles '+inicio+'am') 