# 4ª Crie uma estrutura de repetição (while), com as seguintes funções:
# Cadastrar: Nome, idade e e-mail.
# Listar: Listar todos os dados.
# Alterar: Pedir um nome e realizar a alteração.
# Remoção: Através do nome, remova a pessoa.
# Finalizar: Encerrar o sistema.

# Lista
lista = []

# Variável lógica
continuar = True

# Laço
while continuar:

    # Menu
    print('***MENU***')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Alterar')
    print('4 - Remover')
    print('5 - Sair')
    opcao = int(input())

    # Estrutura de escolha
    match opcao:
        case 1:
            # Perguntas
            print('Informe um nome')
            nome = input()

            print('Informe uma idade')
            idade = int(input())

            print('Informe um e-mail')
            email = input()

            # Dictionary / Objeto
            pessoa = {
                'nome':nome,
                'idade':idade,
                'email':email
            }

            # Cadastrar o objeto na lista
            lista.append(pessoa)

        case 2:
            # Listagem
            for l in lista:
                print('')
                print('Nome: ' + l['nome'])
                print('Idade: ' + str(l['idade']))
                print('E-mail: ' + l['email'])

        case 3:
            # Pedir o nome que será alterado
            print('Informe o nome da pessoa que deseja alterar.')
            nomeAlterado = input()

            # Variável para armazenar o índice do nome a ser alterado
            indiceNomeAlterado = -1

            # Variável índice
            indice = 0

            # Laço de repetição
            for l in lista:
                if l['nome'] == nomeAlterado:
                    indiceNomeAlterado=indice
                indice+=1

            # Verificar se encontrou o nome
            if indiceNomeAlterado == -1:
                print('O nome informado não consta na lista')
            else:
                # Perguntas
                print('Informe um nome')
                nome = input()

                print('Informe uma idade')
                idade = int(input())

                print('Informe um e-mail')
                email = input()

                # Dictionary / Objeto
                pessoa = {
                    'nome':nome,
                    'idade':idade,
                    'email':email
                }

                # Alteração dos dados na lista
                lista[indiceNomeAlterado] = pessoa

        case 4:
            # Pedir o nome que será removido
            print('Informe o nome da pessoa que deseja remover.')
            nomeRemovido = input()

            # Variável para armazenar o índice do nome a ser removido
            indiceNomeRemovido = -1

            # Variável índice
            indice = 0

            # Laço de repetição
            for l in lista:
                if l['nome'] == nomeRemovido:
                    indiceNomeRemovido=indice
                indice+=1

            # Verificar se encontrou o nome
            if indiceNomeRemovido == -1:
                print('O nome informado não consta na lista')
            else:
                # Remvover da lista
                lista.pop(indiceNomeRemovido)

        case 5:
            continuar = False
        case _:
            print('Opção inválida!')