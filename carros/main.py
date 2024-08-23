from db import Carros
from flask import Flask, jsonify, make_response, request

app = Flask('carros')

@app.route("/carros", methods=['GET'])
def get_carros():
    return Carros

@app.route("/carros/<int:id>", methods=['GET'])
def get_carros_by_id(id : int):
    result = {}

    for carro in Carros:
        if carro.get("id") == id:
            result = jsonify(carro)

    return result

@app.route('/carros', methods=['POST'])
def post_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso', carro= carro)
    )
    

@app.route("/carros/<int:id>", methods=['PUT'])
def put_carro(id : int):
    carro_alterado = request.json

    for indice, carro in enumerate(Carros):
        if carro.get("id") == id:
            Carros[indice].update(carro_alterado)

            return jsonify(Carros[indice])

@app.route("/carros/<int:id>", methods=['DELETE'])
def delete_carro(id : int):
    for indice, carro in enumerate(Carros):
        if carro.get("id") == id:
            del Carros[indice]

            return make_response(
                jsonify(mensagem='Carro removido com sucesso')
            )
    

app.run(port=5000, host="localhost")