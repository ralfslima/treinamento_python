# Tuples (tuplas) são listas imutáveis
esportes = ('futebol', 'volei', 'judo', 'basquete')

# Variável nome
nome = ''

# Laço de repetição
while nome != 'sair':

    # Obter o esporte
    print('Informe o esporte que deseja praticar')
    opcao = input()

    # Caso a opção seja sair
    if opcao == 'sair':
        print('Sistema finalizado')
    else:

        # Verificar se o esporte está na tupla
        existe = 0

        for e in esportes:
            if e == opcao:
                existe = 1
                break

        # Retorno
        if existe == 0:
            print('O esporte informado não está disponível')
        else:
            txt = 'Oba! O esporte: {} está disponível'
            print(txt.format(opcao))