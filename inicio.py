from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def index():
    mensagem =  "Estilo do Rei Barbearia"
    return render_template('index.html',mensagem = mensagem)

@app.route('/novofuncionario')
def adicionar_funcionario():
    mensagem = 'Funcionário adicionado !'
    return render_template('novofuncionario.html',mensagem=mensagem)
    
@app.route('/novocliente')
def adicionar_cliente():
    mensagem = "Cliente adicionado"
    return render_template('novocliente.html',mensagem=mensagem)


@app.route('/novoservico')
def adicionar_servico():
    mensagem = "Serviço adicionado"
    return render_template('novoservico.html',mensagem=mensagem)

@app.route('/novoagendamento')
def adicionar_agendamento():
    mensagem = "Agendamento adicionado"
    return render_template('novoagendamento.html',mensagem = mensagem)

@app.route('/login') 
def login():
    mensagem =  "Login efetuado"
    return render_template('login.html',mensagem=mensagem)

@app.route('/logout')
def logout() :
    mensagem ="Encerrando o agendamento..."
    return render_template('logout.html',mensagem = mensa)
app.run(debug=True)