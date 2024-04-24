# Importações
from flask import Flask, render_template, request

# Criar o APP
app = Flask(__name__)

# ***************************** ATIVIDADE 01 *****************************
# Formulário da atividade 1
@app.route('/atividade1')
def atividade1():
    return render_template('atividade1.html')

# Rota para receber os dados vindos do formulário
@app.route('/resultado_atividade1', methods=['POST'])
def resultado_atividade1():
    # Obter o nome e as notas informados no formulário
    nome = request.form['nome']
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])

    # Realizar a média
    media = (nota1+nota2)/2

    # Retorno
    return nome + ' obteve a média ' + str(media) + '.'


# ***************************** ATIVIDADE 02 *****************************
# Formulário da atividade 2
@app.route('/atividade2')
def atividade2():
    return render_template('atividade2.html')

# Rota para receber os dados vindos do formulário
@app.route('/resultado_atividade2', methods=['POST'])
def resultado_atividade2():
    # Obter a cidade
    cidade = int(request.form['cidade'])

    # Estrutura de escolha
    match cidade:
        case 1:
            return 'São Paulo, centro financeiro do Brasil, está entre as cidades mais populosas do mundo, com diversas instituições culturais e uma rica tradição arquitetônica.'
        
        case 2:
            return 'O Rio de Janeiro é uma grande cidade brasileira à beira-mar, famosa pelas praias de Copacabana e Ipanema, pela estátua de 38 metros de altura do Cristo Redentor, no topo do Corcovado, e pelo Pão de Açúcar, um pico de granito com teleféricos até seu cume.'
        
        case 3:
            return 'Curitiba é a capital do estado do Paraná, na região sul do Brasil. A Torre Panorâmica, que tem um observatório em sua parte superior, destaca-se na silhueta da cidade.'
        
        case 4:
            return 'Salvador, inicialmente São Salvador da Bahia de Todos os Santos, é um município brasileiro, capital do estado da Bahia e primeira capital do Brasil. Fundada em 29 de março de 1549 por Tomé de Sousa, por conta da implantação do Governo-Geral do Brasil pelo Império Português,[8] a cidade está entre as mais antigas do continente americano e é uma das primeiras cidades planejadas no mundo, ainda no período do Renascimento.'
        
        case 5:
            return 'Porto Alegre é a capital do estado de Rio Grande do Sul, no sul do Brasil. Na praça principal, a Praça Marechal Deodoro, encontra-se a Catedral Metropolitana, de estilo renascentista, com murais religiosos no exterior.'
        
        case _:
            return 'Escolha uma cidade!'
        

# ***************************** ATIVIDADE 03 *****************************
# Formulário da atividade 3
@app.route('/atividade3')
def atividade3():
    return render_template('atividade3.html')

# Rota para receber os dados vindos do formulário
@app.route('/resultado_atividade3', methods=['POST'])
def resultado_atividade3():
    # Obter o número para realizar a tabuada
    numero = int(request.form['numero'])

    # Realizar a tabuada
    tabuada = 'A tabuada de ' + str(numero) + ' é: <hr><ul>'
    
    for indice in range(0, 11):
        tabuada += '<li>' + str(numero) + ' X ' + str(indice) + ' = ' + str(numero*indice) + '</li>'
    
    tabuada+='</ul>'

    # Retorno
    return tabuada


# ***************************** ATIVIDADE 04 *****************************
# Formulário da atividade 4
@app.route('/atividade4')
def atividade4():
    return render_template('atividade4.html')

# Rota para receber os dados vindos do formulário
@app.route('/resultado_atividade4', methods=['POST'])
def resultado_atividade4():
    # Obter o texto informado
    texto = request.form['texto']

    # Contabilizar vogais e consoantes
    vogais = 0
    consoantes = 0

    for caractere in texto.lower():
        # Caso seja um espaço, não será contabilizado
        if caractere != ' ':
            # Verificar se é consoante ou vogal
            if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
                vogais += 1
            else:
                consoantes += 1

    # Estrutura de exibição
    retorno = '<h1>Vogais: '+ str(vogais) +'</h1>'
    retorno += '<h1>Consoantes: '+ str(consoantes) +'</h1>'
    
    # Retorno
    return retorno


# ***************************** ATIVIDADE 05 *****************************
# Formulário da atividade 5
@app.route('/atividade5')
def atividade5():
    return render_template('atividade5.html')

# Rota para receber os dados vindos do formulário
@app.route('/resultado_atividade5', methods=['POST'])
def resultado_atividade5():
    # Obter o nome, email e idade informados no formulário
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']

    # Variável para verificar se alguma validação foi realizada
    valiadacaoRealizada = False

    # Validações
    validacoes = "<ul>"

    # Validação - Campos vazios
    if nome == '':
        validacoes += '<li>O campo nome está vazio!</li>'
        valiadacaoRealizada = True
    
    if email == '':
        validacoes += '<li>O campo e-mail está vazio!</li>'
        valiadacaoRealizada = True
    
    if idade == '':
        validacoes += '<li>O campo idade está vazio!</li>'
        valiadacaoRealizada = True

    # Validação - Nome precisa ter pelo menos 3 caracteres
    if len(nome) < 3:
        validacoes += '<li>O nome precisa conter pelo menos 3 caracteres!</li>'
        valiadacaoRealizada = True

    # Validação - E-mail precisa conter @ e .
    if not '@' in email or not '.' in email:
        validacoes += '<li>O e-mail precisa conter @ e .</li>'
        valiadacaoRealizada = True

    # Validação - Idade é um número
    try:
        if int(idade) < 0:
            validacoes += '<li>A idade não pode ser inferior a 0.</li>'
            valiadacaoRealizada = True
    except:
        validacoes += '<li>A idade não pode ser inferior a 0.</li>'
        validacoes += '<li>A idade precisa ser um número</li>'
        valiadacaoRealizada = True

    # Finalizar a lista de validação
    validacoes += '</ul>'

    # Caso todas as validações estejam ok
    if valiadacaoRealizada == False:
        return '<h1>Parabéns! Formulário devidamente preenchido.</h1>'
    else:
        return validacoes


# ***************************** ATIVIDADE 06 - EXTRA *****************************
# Lista de nomes
nomes = []

# Formulário da atividade 6
@app.route('/atividade6', methods=['POST', 'GET'])
def atividade6():
    # Verificar se é uma requisição GET ou POST
    if request.method == 'GET':
        return render_template('atividade6.html', lista=nomes, quantidade=len(nomes))
    else:
        nomes.append(request.form['nome'])
        return render_template('atividade6.html', lista=nomes, quantidade=len(nomes))

# Rota para remover os nomes
@app.route('/remover/<indice>')
def remover(indice):
    # Remover o nome da lista
    nomes.pop(int(indice))

    # Retorno
    return atividade6()

# Execução do projeto (servidor)
if __name__ == '__main__':
    app.run()