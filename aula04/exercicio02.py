# Criar um sistema para gerenciar pessoas
# CRUD - Create, Read, Update e Delete

# Lista (Agrupamento de dados)
nomes = []

# Opção (Para saber o que será feito)
opcao = 0

# *************** Função de cadastro
def cadastrar():
    print('Informe um nome para cadastrar.')
    nomes.append(input())
    #nome = input()
    #nomes.append(nome)

# *************** Função para listar
def listar():
    print('Listagem:')
    for n in nomes:
        print(n)

# *************** Função para alterar
def alterar():
    print('Informe a posição do vetor que seja alterar.')
    posicao = int(input())

    print('Informe o novo nome.')
    nomes[posicao] = input()

# *************** Função para remover
def remover():
    print('Informe a posição do vetor que seja remover.')
    nomes.pop(int(input()))
    #posicao = int(input())
    #nomes.pop(posicao)

# *************** Função para exibir o menu
def menu():
    print('*** MENU ***')
    print('1º Cadastrar')
    print('2º Listar')
    print('3º Alterar')
    print('4º Remover')
    print('5º Sair do sistema')

# Laço
while opcao != 5:

    # Opções
    menu()
    opcao = int(input())

    # Ações
    match opcao:
        case 1:
            cadastrar()

        case 2:
            listar()

        case 3:
            alterar()

        case 4:
            remover()

        case 5:
            print('Sistema finalizado!')

        case _:
            print('Opção inválida')