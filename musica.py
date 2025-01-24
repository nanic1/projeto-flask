from flask import Flask, render_template

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero

app = Flask(__name__)

@app.route('/inicio')
def hello():
    return '<h1>Hello world</h1>'

@app.route('/musicas')
def listarMusicas():

    musica01 = Musica('Temporal', 'Hungria', 'Rap')
    musica02 = Musica('Papai banca', 'Mc Ryan SP', 'Funk')
    musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')

    lista = [musica01, musica02, musica03]

    return render_template('lista_musica.html',
                           titulo = 'Aprendendo do início com Pedro Kurtz',
                           musicas = lista)


app.run(debug=True)