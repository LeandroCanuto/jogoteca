from flask import Flask,render_template,request , redirect , session , flash ,url_for

class Jogo:
        def __init__(self, nome,categoria, console):
                self.nome=nome
                self.categoria=categoria
                self.console=console

jogo1 = Jogo('Tetris', 'Puzzle' , 'Atari')
jogo2 = Jogo('God of War  ', ' Rack n slash ', 'PS2')
jogo3 = Jogo('Mortal Kombat ', ' Luta ', 'PS2')
lista = [jogo1, jogo2 ,jogo3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return  render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso! ')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():

    flash('Logout efetuado com sucesso.Até mais  ' + session['usuario_logado'] + '  !!!')
    session['usuario_logado'] = None
    return redirect(url_for('index'))



app.run(port=4996,debug=True)