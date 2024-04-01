# Criar um sistema de votação, haverá 4 candidatos
# Ao término da votação, informe a quantidade de votos
# de cada um e o vencedor (haverá apenas um vencedor)

# Contadores
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0

# Variável voto
voto = 0

# Laço enquanto (while)
while voto != 5:
    
    # Mensagem
    print('**** VOTAÇÃO ****')
    print('1 - Candidato 01')
    print('2 - Candidato 02')
    print('3 - Candidato 03')
    print('4 - Candidato 04')
    print('5 - Finalizar votação')
    voto = int(input())

    # Contabilização
    # if voto == 1:
    #     cand1 += cand1 + 1
    # elif voto == 2:
    #     cand2 += cand2 + 1
    # elif voto == 3:
    #     cand3 += cand3 + 1
    # elif voto == 4:
    #     cand4 += cand4 + 1
    # elif voto == 5:
    #     print('Votação finalizada')
    # else:
    #     print('Opção inválida, tente novamente')

    match(voto):
        case 1:
            cand1 += 1
        case 2:
            cand2 += 1
        case 3:
            cand3 += 1
        case 4:
            cand4 += 1
        case 5:
            print('Votação finalizada')
        case _:
            print('Opção inválida, tente novamente')

# Exibir a quantidade de votos por candidato
print('Candidato 01 teve: '+str(cand1)+' votos.')
print('Candidato 02 teve: '+str(cand2)+' votos.')
print('Candidato 03 teve: '+str(cand3)+' votos.')
print('Candidato 04 teve: '+str(cand4)+' votos.')

# Exibir o vencedor (NÃO FUNCIONA EM CASO DE EMPATE)
# if cand1 > cand2 and cand1 > cand3 and cand1 > cand4:
#     print('O vencedor é o candidato01')
# elif cand2 > cand1 and cand2 > cand3 and cand2 > cand4:
#     print('O vencedor é o candidato02')
# elif cand3 > cand1 and cand3 > cand2 and cand3 > cand4:
#     print('O vencedor é o candidato03')
# else:
#     print('O vencedor é o candidato04')

# Exibir os vencedores (FUNCIONA EM CASO DE EMPATE)
maiorVoto = cand1

if cand2 > maiorVoto:
    maiorVoto = cand2

if cand3 > maiorVoto:
    maiorVoto = cand3

if cand4 > maiorVoto:
    maiorVoto = cand4

print('**** RESULTADO ****')

contador = 0

if cand1 == maiorVoto:
    print('Candidato01')
    contador += 1

if cand2 == maiorVoto:
    print('Candidato02')
    contador += 1

if cand3 == maiorVoto:
    print('Candidato03')
    contador += 1

if cand4 == maiorVoto:
    print('Candidato04')
    contador += 1

if contador == 1:
    print('Status da eleição: Decidido em 1º turno')
else:
    print('Status da eleição: Emparte - Haverá 2º turno')