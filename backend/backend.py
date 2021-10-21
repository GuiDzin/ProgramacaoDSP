from operator import truediv
from config import *
from modelo import Pokemon

@app.route("/")
def inicio():
    return 'Sistema de Cadastro de Pokemons.' +\
        '<a href= "/listar_pokemons">Operação listar</a>'


@app.route("/listar_pokemons")
def listar_pokemons():
    #Obter os Pokemons do cadastro
    pokemon = db.session.query(Pokemon).all()
    #Aplica Json a cada elemento da Lista Pokemon
    pokemon_em_json = [x.json() for x in pokemon]
    #Converte a lista Python para Json
    resposta = jsonify(pokemon_em_json)
    #Permite enviar para qualquer solicitante
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    #Retorno
    return resposta

app.run(debug=True)