from flask import Flask, render_template, request, redirect, session

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero

musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan SP', 'Funk')
musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]

app = Flask(__name__)

app.secret_key = 'Batata123#'

@app.route('/inicio')
def hello():
    return '<h1>Hello world</h1>'

@app.route('/')
def listarMusicas():

    return render_template('lista_musica.html',
                           titulo = 'Aprendendo do início com Pedro Kurtz',
                           musicas = lista)



@app.route('/cadastrar')
def cadastrarMusicas():
    return render_template('cadastro_musicas.html')

@app.route('/add', methods=['POST',])
def adicionarMusicas():
    nome = request.form['txtNome']
    cantor = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantor, genero)

    lista.append(novaMusica)

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senhaUser'] == 'admin':

        session['paginaLogin'] = request.form['nomeUser']

        return redirect('/')
    else:
        return redirect('/login')

@app.route('/sair')
def sair():
    session['paginaLogin'] = None

    return redirect('/')

app.run(debug=True)