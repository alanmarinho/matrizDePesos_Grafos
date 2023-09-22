import os
from flask import Flask, jsonify, render_template, request
from backend.grafo import calcula_matriz

app = Flask(__name__, static_folder='frontend', static_url_path='/frontend')

@app.route('/')
def index(): 
    pasta_arquivos = "./instancias"
    arquivos_disponiveis = os.listdir(pasta_arquivos)
    return render_template('index.html', arquivos=arquivos_disponiveis)

@app.route('/api/matriz', methods=['GET'])
def get_matriz():
    nome_arquivo = request.args.get('arquivo')
    if nome_arquivo is None:
        return jsonify({"error": "Nome do arquivo não fornecido"}), 400
    matriz_ponderada, num_vertices = calcula_matriz(nome_arquivo)

    resposta = {
        "matriz_ponderada": matriz_ponderada,
        "num_vertices": num_vertices
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run()
