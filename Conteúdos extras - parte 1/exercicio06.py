# 6ª Peça uma cidade e retorne informação da cidade selecionada

# Obter a cidade
print('Informe o número da cidade:')
print('1) São Paulo')
print('2) Rio de Janeiro')
print('3) Brasília')
cidade = int(input())

# Estrutura de escolha
match cidade:
    case 1:
        print('São Paulo, centro financeiro do Brasil, está entre as cidades mais populosas do mundo, com diversas instituições culturais e uma rica tradição arquitetônica.')
    case 2:
        print('O Rio de Janeiro é uma grande cidade brasileira à beira-mar, famosa pelas praias de Copacabana e Ipanema, pela estátua de 38 metros de altura do Cristo Redentor, no topo do Corcovado, e pelo Pão de Açúcar, um pico de granito com teleféricos até seu cume.')
    case 3:
        print('Brasília  é a capital federal do Brasil e a sede de governo do Distrito Federal.[7] A capital está localizada na região Centro-Oeste do país, ao longo da região geográfica conhecida como Planalto Central.')
    case _:
        print('Cidade não encontrada.')