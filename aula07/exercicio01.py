# Criar um sistema para cadastrar alunos.
# Cadastro: Nome, duas notas e turno.
# Listagem: Exibir nome, média e turno.
# Estatísticas: Quantidade de alunos por turno e por média (situação)
# Alterar: Alterar nome e notas.
# Remover: Remoção através do nome.

# ------------- LISTA E VARIÁVEIS ----------------- #

# Lista de alunos (dicionários/dictionary)
alunos = []

# Contadores
matutino = 0
vespertino = 0
noturno = 0

aprovado = 0
exame = 0
reprovado = 0

# ------------- FUNÇÃO PARA RETORNAR UM DICTIONARY - #
def objAluno():
    # Realizar perguntas
    print('Informe o nome do aluno')
    nome = input()

    print('Informe a 1ª nota')
    nota1 = float(input())

    print('Informe a 2ª nota')
    nota2 = float(input())

    print('Informe o número correspondente ao turno')
    print('1º Matutino')
    print('2º Vespertino')
    print('3º Noturno')
    turno = int(input())

    # Realizar a média
    media = (nota1+nota2)/2

    # Dicionário (objeto)
    obj = {
        'nome':nome,
        'nota1':nota1,
        'nota2':nota2,
        'media':media,
        'turno':turno
    }

    # Retornar um dicionário
    return obj



# ------------- FUNÇÃO DE CADASTRO ----------------- #
def cadastro():
    # Variáveis globais
    global aprovado
    global exame
    global reprovado
    global matutino
    global vespertino
    global noturno

    # Executar a função para retornar um objeto do tipo dictionary (aluno)
    obj = objAluno()

    # Contabilizar média (situação)
    if obj['media'] >= 7:
       aprovado = aprovado + 1
    elif obj['media'] >= 5:
        exame = exame + 1
    else:
        reprovado = reprovado + 1

    # Contabilizar turno
    if obj['turno'] == 1:
        matutino = matutino + 1
    elif obj['turno'] == 2:
        vespertino = vespertino + 1
    else:
        noturno = noturno + 1

    

    # Cadastrar na lista
    alunos.append(obj)

# ------------- FUNÇÃO DE LISTAGEM ----------------- #
def listagem():
    # Listagem de alunos
    for a in alunos:
        print('')
        print('Nome: '  + a['nome'] )
        print('Média: ' + str(a['media']))

        match(a['turno']):
            case 1:
                print('Turno: matutino')
            case 2:
                print('Turno: vespertino')
            case 3:
                print('Turno: noturno')

# ------------- FUNÇÃO DE ESTATÍSTICAS ------------- #
def estatistica():
    # Quantidade de alunos por média (situação)
    print('Aprovados: ' + str(aprovado))
    print('Em exame: ' + str(exame))
    print('Reprovados: ' + str(reprovado))
    print('')

    # Quantidade de alunos por turno
    print('Matutino: ' + str(matutino))
    print('Vespertino: ' + str(vespertino))
    print('Noturno: ' + str(noturno))
    print('')

    # Percentual
    total = aprovado+exame+reprovado

    print(str(100/total*aprovado)+'% estão aprovados')
    print(str(100/total*exame)+'% estão em exame')
    print(str(100/total*reprovado)+'% estão reprovados')
    print('')

    print(str(100/total*matutino)+'% estão no turno matutino')
    print(str(100/total*vespertino)+'% estão no turno vespertino')
    print(str(100/total*noturno)+'% estão no turno noturno')
    print('')

# ------------- FUNÇÃO DE ALTERAÇÃO ---------------- #
def alterar():
    # Variáveis globais
    global matutino
    global vespertino
    global noturno
    global aprovado
    global exame
    global reprovado

    # Obter o nome do aluno que será alterado
    print('Informe o nome do aluno que será alterado')
    nomeAlterado = input()

    # Obter a posição do nome
    posicao = -1
    contador = 0

    for a in alunos:
        if a['nome'] == nomeAlterado:
            posicao = contador
        else:
            contador+=1

    # Condicional
    if posicao == -1:
        print('Aluno não encontrado')
    else:
        # Excluir a situação de média
        if alunos[posicao]['media'] >= 7:
            aprovado-=1
        elif alunos[posicao]['media'] >= 5:
            exame-=1
        else:
            reprovado-=1

        # Excluir o turno
        match(alunos[posicao]['turno']):
            case 1:
                matutino-=1
            case 2:
                vespertino-=1
            case 3:
                noturno-=1

        # Executar a função para retornar um objeto do tipo dictionary (aluno)
        obj = objAluno()

        # Contabilizar média (situação)
        if obj['media'] >= 7:
            aprovado+=1
        elif obj['media'] >= 5:
            exame+=1
        else:
            reprovado+=1

        # Contabilizar turno
        if obj['turno'] == 1:
            matutino+=1
        elif obj['turno'] == 2:
            vespertino+=1
        else:
            noturno+=1

        # Alterar o aluno na lista
        alunos[posicao] = obj

# ------------- FUNÇÃO DE REMOÇÃO ------------------ #
def remover():
    # Variáveis globais
    global matutino
    global vespertino
    global noturno
    global aprovado
    global exame
    global reprovado

    # Obter o nome do aluno que será removido
    print('Informe o nome do aluno que será removido')
    nomeRemovido = input()

    # Obter a posição do nome
    posicao = -1
    contador = 0

    for a in alunos:
        if a['nome'] == nomeRemovido:
            posicao = contador
        else:
            contador+=1

    # Condicional
    if posicao == -1:
        print('O nome informado não existe.')
    else:

        # Obter a média do aluno
        media = alunos[posicao]['media']

        # Contabilizar média (situação)
        if media >= 7:
            aprovado-=1
        elif media >= 5:
            exame-=1
        else:
            reprovado-=1

        # Contabilizar turno
        if alunos[posicao]['turno'] == 1:
            matutino-=1
        elif alunos[posicao]['turno'] == 2:
            vespertino-=1
        else:
            noturno-=1

        alunos.pop(posicao)

# ------------- ESTRUTURA PRINCIPAL ---------------- #

# Variável contendo uma opção de ação
opcao = 0

# Laço
while opcao != 6:

    # Perguntar a ação que será executada
    print('O que deseja fazer?')
    print('1º Cadastrar')
    print('2º Listar')
    print('3º Estatísticas')
    print('4º Alterar')
    print('5º Remover')
    print('6º Sair')
    opcao = int(input())

    # Ações
    match(opcao):
        case 1:
            # Executar função para cadastrar alunos
            cadastro()

        case 2:
            # Executar função para listar alunos
            listagem()
            
        case 3:
            # Executar a função de estatística
            estatistica()

        case 4:
            # Executar a função para alterar alunos
            alterar()
                    
        case 5:
            # Executar a função para remover alunos
            remover()

        case 6:
            print('Você saiu do sistema.')
        
        case _:
            print('Opção inválida.')