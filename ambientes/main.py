from db import Ambientes
from flask import Flask, jsonify, make_response, request

app = Flask("ambientes")

messageNoFound = make_response(
    jsonify(mensagem='Ambiente nao encontrado')
)

@app.route("/ambientes", methods=['GET'])
def get_ambientes():
    return Ambientes

@app.route("/ambientes/<int:id>", methods=["GET"])
def get_ambiente_by_id(id : int):
    for ambiente in Ambientes:
        if ambiente.get("id") == id:
            return jsonify(ambiente)
    
    return messageNoFound

@app.route("/ambientes", methods=["POST"])
def create_ambiente():
    new_ambiente = request.json

    for ambiente in Ambientes:
        if ambiente.get("id") == new_ambiente.get("id"):
            return make_response(
                jsonify(mensagem='Ambiente já existente')
            )

    Ambientes.append(new_ambiente)
    return make_response(
        jsonify(mensagem='Ambiente cadastrado com sucesso', ambiente=new_ambiente)
    )

@app.route("/ambientes/<int:id>", methods=["PUT"])
def update_ambiente(id : int):
    new_ambiente = request.json

    for index, ambiente in enumerate(Ambientes):
        if ambiente.get("id") == id:
            Ambientes[index].update(new_ambiente)

            return make_response(
                jsonify(mensagem='Ambiente editado com sucesso')
            )
        
    return messageNoFound

@app.route("/ambientes/<int:id>", methods=["PUT"])
def delete_ambiente(id : int):
    for index, ambiente in enumerate(Ambientes):
        if ambiente.get("id") == id:
            del Ambientes[index]

            return make_response(
                jsonify(mensagem='Ambiente deletado com sucesso')
            )

    return messageNoFound

app.run(port=5000, host="localhost")