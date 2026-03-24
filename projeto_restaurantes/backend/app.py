from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
Swagger(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone
        }

with app.app_context():
    db.create_all()

@app.route('/api/restaurantes', methods=['GET'])
def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.
    ---
    responses:
      200:
        description: Uma lista de restaurantes
    """
    restaurantes = Restaurante.query.all()
    # transformar os objetos Restaurante em dicionários para retornar como JSON
    return jsonify([restaurante.to_dict() for restaurante in restaurantes])

@app.route('/api/restaurantes', methods=['POST'])
def cadastrar_restaurante():
    """
    Cadastra um novo restaurante.
    ---
    parameters:
      - in: body
        name: restaurante
        description: Dados do novo restaurante
        schema:
          type: object
          required:
            - nome
            - endereco
            - telefone
          properties:
            nome:
              type: string
              example: "Pizzaria do Bairro"
            endereco:
              type: string
              example: "Rua das Flores, 123"
            telefone:
              type: string
              example: "9999-8888"
    responses:
      201:
        description: Restaurante cadastrado com sucesso
    """
    dados = request.json()

    novo_restaurante = Restaurante(
        nome=dados['nome'],
        endereco=dados['endereco'],
        telefone=dados['telefone']
    )
    db.session.add(novo_restaurante)
    db.session.commit()
    # retornar o restaurante recém-cadastrado como resposta
    return jsonify({
        'message': 'Restaurante cadastrado com sucesso!',
        'restaurante': novo_restaurante.to_dict()
    }), 201  # status code 201 indica que um recurso foi criado com sucesso

if __name__ == '__main__':
    app.run(debug=True, port=5000)
