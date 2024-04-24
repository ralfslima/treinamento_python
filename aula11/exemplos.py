# Importações
from flask import Flask, render_template, request

# Criar o APP
app = Flask(__name__)

# Rota (localhost:5000)
@app.route('/')
def inicio():
    return 'Hello World!'

# Rota para concatenar
@app.route('/<nome>')
def concatenacao(nome):
    return 'Boa noite ' + nome

# Rota para exibir uma página HTML
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

# Rota para exibir uma página HTML e concatenar com uma variável
@app.route('/pagina2/<nome>')
def pagina2(nome):
    return render_template('pagina2.html', nomeDaPessoa=nome)

# Rota para exibir um formulário
@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

# Rota para receber os dados vindos do formulário
@app.route('/receberFormulario', methods=['POST'])
def receberFormulario():
    # Obter o nome e a idade informados no formulário
    nome = request.form['nome']
    idade = request.form['idade']

    # Retorno
    return 'Olá ' + nome + ' você tem ' + idade + ' anos.'

# Execução do projeto (servidor)
if __name__ == '__main__':
    app.run()