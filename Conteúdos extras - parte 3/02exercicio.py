# Crie uma estrutura de repetição (while) que peça uma cor.
# Após pedir uma cor, pergunte se deseja continuar a perguntar uma nova cor.
# Após sair do laço, informe as cores cadastradas

# Lista de cores
lista = []

# Variável lógica
continuar = True

# Laço
while continuar:
    # Obter uma cor
    print('Informe uma cor')
    lista.append(input())

    # Continuar
    print('Deseja informar mais uma cor? 1-SIM | 2-NÃO')
    verificar = int(input())

    if verificar == 2:
        continuar = False

# Listar as cores cadastradas
for l in lista:
    print(l)