from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.repositories.figurinhas_repo import FigurinhaRepository
from app.services.figurinhas_service import (
    CreateFigurinhaService,
    ListFigurinhasService,
    GetFigurinhaByIdService,
    DeleteFigurinhaService, 
    AtualizaFigurinhaService
)

figurinha_blueprint = Blueprint('figurinha', __name__)

repo = FigurinhaRepository()
create_service = CreateFigurinhaService(repo)
list_service = ListFigurinhasService(repo)
get_by_id_service = GetFigurinhaByIdService(repo)
delete_service = DeleteFigurinhaService(repo)
atualiza_figurinha = AtualizaFigurinhaService(repo)


@figurinha_blueprint.route('/figurinha', methods=['POST'])
def create_figurinha():
    """
    Cria uma nova figurinha
    ---
    tags:
      - Figurinhas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            numero:
              type: string
              example: "42"
              
            posicao:
              type: string
              enum: [goleiro, zagueiro, meio-campista, atacante]
              example: "atacante"
              
            tipo:
                type: string
                enum: [legends_ouro, legends_bronze, brilhante, comum]
                example: "comum"
    responses:
      201:
        description: Figurinha criada com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json() or {}
    try:
        nova_figurinha = create_service.execute(
            numero=data.get('numero'),
            posicao=data.get('posicao'),
            tipo=data.get('tipo')
        )
        return jsonify({
            "id": nova_figurinha.id,
            "numero": nova_figurinha.numero,
            "posicao": nova_figurinha.posicao,
            "tipo": nova_figurinha.tipo, 
            "created_at": nova_figurinha.created_at, 
            "updated_at": nova_figurinha.updated_at
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@figurinha_blueprint.route('/figurinha/<int:id>', methods=['GET'])
def get_figurinha(id: int):
    """
    Busca uma figurinha pelo ID
    ---
    tags:
      - Figurinhas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Figurinha encontrada
      404:
        description: figurinha não encontrado
    """
    try:
        figurinha = get_by_id_service.execute(id)
    except ValueError:
        return jsonify({"error": "figurinha não encontrado"}), 404
    
    return jsonify({
        "id": figurinha.id,
        "numero": figurinha.numero,
        "tipo": figurinha.tipo,
        "posicao": figurinha.posicao, 
        "created_at": figurinha.created_at, 
        "updated_at": figurinha.updated_at
    }), 200

@figurinha_blueprint.route('/figurinha', methods=['GET'])
def list_figurinhas():
    """
    Lista todas as figurinhas
    ---
    tags:
      - Figurinhas
    parameters:
      - in: query
        name: tipo
        type: string
        enum: [legends_ouro, legends_bronze, brilhante, comum]
        required: false
      - in: query
        name: posicao
        type: string
        enum: [goleiro, zagueiro, meio-campista, atacante]
        required: false
    responses:
      200:
        description: Lista de figurinhas
    """
    tipo = request.args.get('tipo')
    posicao = request.args.get('posicao')
    
    try:
        figurinhas = list_service.execute(tipo=tipo, posicao=posicao)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    output = [
        {
            "id": f.id,
            "numero": f.numero,
            "posicao": f.posicao,
            "tipo": f.tipo,
            "created_at": f.created_at.isoformat(),
            "updated_at": f.updated_at.isoformat()
        }
        for f in figurinhas
    ]
    return jsonify(output), 200


@figurinha_blueprint.route('/figurinha/<int:id>', methods=['DELETE'])
def delete_figurinha(id: int):
    """
    Deleta uma figurinha pelo ID
    ---
    tags:
      - Figurinhas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Figurinha deletada com sucesso
      404:
        description: figurinha não encontrado
    """
    try:
        figurinha = get_by_id_service.execute(id)
    except ValueError:
        return jsonify({"error": "figurinha não encontrado"}), 404

    delete_service.execute(id)
    return "", 204

@figurinha_blueprint.route("/figurinha/<int:id>", methods=['PUT'])
def update_figurinha(id: int):
    """
    Atualiza uma figurinha
    ---
    tags:
      - Figurinhas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          properties:
            numero:
              type: string
              example: "42"
              
            posicao:
              type: string
              enum: [goleiro, zagueiro, meio-campista, atacante]
              example: "atacante"
              
            tipo:
                type: string
                enum: [legends_ouro, legends_bronze, brilhante, comum]
                example: "comum"
    responses:
      200:
        description: Figurinha atualizada com sucesso
      400:
        description: Dados inválidos
      404:
        description: figurinha não encontrado
    """
    try:
        get_by_id_service.execute(id)
    except ValueError:
        return jsonify({"error": "figurinha não encontrado"}), 404

    data = request.get_json() or {}
    try:
        figurinha = atualiza_figurinha.execute(
            figurinha_id=id,
            numero=data.get('numero'),
            posicao=data.get('posicao'),
            tipo=data.get('tipo')
        )
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "id": figurinha.id,
        "numero": figurinha.numero,
        "tipo": figurinha.tipo,
        "posicao": figurinha.posicao,
        "created_at": figurinha.created_at.isoformat(),
        "updated_at": figurinha.updated_at.isoformat()
    }), 200