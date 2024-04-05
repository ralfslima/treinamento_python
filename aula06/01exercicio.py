# Criar um gerenciamento de produtos.

# Lista para armazenar os produtos
produtos = []

# Variável acao
acao = 0

# Função para retornar a posição do produto na lista
def posicaoProduto(nome):
    obterIndice = -1
    contador = 0

    for p in produtos:
        if p['nome'] == nome:
            obterIndice = contador
        contador+=1

    return obterIndice

# Função para realizar o cadastro
def cadastro():
    # Obter os dados do produto
    print('Informe o nome do produto.')
    nome = input()

    print('Informe a marca do produto.')
    marca = input()

    print('Informe o valor do produto.')
    valor = float(input())

    # Criar dictionary
    produto = {
        'nome' :nome,
        'marca':marca,
        'valor':valor
    }

    # Cadastrar dictionary na lista
    produtos.append(produto)

# Função para selecionar todos os produtos
def selecao():
    for p in produtos:
        print('Nome:  ' + p['nome'])
        print('Marca: ' + p['marca'])
        print('Valor: ' + str( p['valor']))
        print('')

# Função para alterar produtos
def alteracao():
    # Obter o nome do produto que será alterado
    print('Informe o nome do produto que será alterado')
    produtoAlterado = input()

    # Verificar a posição do produto
    posicao = posicaoProduto(produtoAlterado)

    # Condição
    if posicao == -1:
        print('Produto não encontrado.')
    else:
        # Obter os dados do produto
        print('Informe o nome do produto.')
        nome = input()

        print('Informe a marca do produto.')
        marca = input()

        print('Informe o valor do produto.')
        valor = float(input())

        # Criar dictionary
        produto = {
            'nome' :nome,
            'marca':marca,
            'valor':valor
        }

        # Alteração na lista
        produtos[posicao] = produto

# Função para remover produtos
def remocao():
    # Obter o nome do produto que será removido
    print('Informe o nome do produto que será removido')
    produtoRemovido = input()

    # Verificar se o produto informado existe na lista
    posicao = posicaoProduto(produtoRemovido)

    # Condicional
    if posicao == -1:
        print('Produto não encontrado.')
    else:
        produtos.pop(posicao)


    

# Laço de repetição
while acao != 5:

    # Obter a ação
    print('O que deseja fazer?')
    print('1) Cadastrar produtos')
    print('2) Selecionar produtos')
    print('3) Alterar produtos')
    print('4) Remover produtos')
    print('5) Sair do sistema')
    acao = int(input())

    # Executar ações
    match acao:
        case 1:
            cadastro()
        case 2:
            selecao()
        case 3:
            alteracao()
        case 4:
            remocao()
        case 5:
            print('Obrigado por utilizar o sistema!')
        case _:
            print('Opção inválida')