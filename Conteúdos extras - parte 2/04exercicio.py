# 4ª Informe 4 cidades, o cliente poderá escolher uma delas ou a opção SAIR.
# Enquanto não informada a opção SAIR, peça uma cidade.
# Quando finalizar o sistema, exiba a quantidade selecionada de cada cidade.

# Contadores
saoPaulo = 0
rioDeJaneiro = 0
curitiba = 0
beloHorizonte = 0

# Continuar laço
continuar = True

# Laço de repetição
while continuar:
    
    # Valida opção
    validaOpcao = True
    while validaOpcao:
        try:
            # Menu
            print('Escolha uma cidade')
            print('1) São Paulo')
            print('2) Rio de Janeiro')
            print('3) Curitiba')
            print('4) Belo Horizonte')
            print('5) Sair')
            opcao = int(input())

            validaOpcao = False
        except:
            print('Informe um número entre 1 e 5')

    # Estrutura de escolha
    match(opcao):
        case 1:
            saoPaulo+=1
        case 2:
            rioDeJaneiro+=1
        case 3:
            curitiba+=1
        case 4:
            beloHorizonte+=1
        case 5:
            continuar = False
        case _:
            print('Opção inválida')

# Exibir os votos para cada cidade
print('São Paulo obteve: ' +str(saoPaulo)+ ' votos.')
print('Rio de Janeiro obteve: ' +str(rioDeJaneiro)+ ' votos.')
print('Curitiba obteve: ' +str(curitiba)+ ' votos.')
print('Belo Horizonte obteve: ' +str(beloHorizonte)+ ' votos.')