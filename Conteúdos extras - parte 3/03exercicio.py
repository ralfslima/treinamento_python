# 3ª Crie uma estrutura de repetição (while) com as seguintes funções:
# Cadastrar: Cadastrar um nome na lista
# Remover: Através do nome, remova da lista
# Finalizar: Encerra o laço de repetição
# Após finalizar o laço, exiba todos os nomes

# Lista
nomes = []

# Variável lógica para o laço de repetição
continuar = True

# Laço
while continuar:

    # Menu
    print('***MENU****')
    print('1) Cadastrar')
    print('2) Remover')
    print('3) Finalizar')
    opcao = int(input())

    # Estrutura de escolha
    match opcao:
        case 1:
            print('Informe um nome')
            nomes.append(input())
        case 2:
            print('Informe o nome da pessoa a ser excluída')
            nome = input()

            existeNome = False

            for n in nomes:
                if n == nome:
                    existeNome = True
                    nomes.remove(nome)

            if existeNome == True:
                print('Nome removido da lista!')
            else:
                print('Nome não encontrado!')
        case 3:
            continuar = False
        case _:
            print('Opção inválida')

# Listagem de nomes
for n in nomes:
    print(n)