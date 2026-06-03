from flask import Blueprint, request, jsonify
from repositories.figurinhas_repo import FigurinhaRepository
from services.figurinhas_service import (
    CreateFigurinhaService,
    ListFigurinhasService,
    GetFigurinhaByIdService,
    DeleteFigurinhaService
)

figurinha_blueprint = Blueprint('figurinhas', __name__)

repo = FigurinhaRepository()
create_service = CreateFigurinhaService(repo)
list_service = ListFigurinhasService(repo)
get_by_id_service = GetFigurinhaByIdService(repo)
delete_service = DeleteFigurinhaService(repo)


@figurinha_blueprint.route('/figurinhas', methods=['POST'])
def create_figurinha():
    data = request.get_json() or {}
    
    try:
        nova_figurinha = create_service.execute(
            numero=data.get('numero'),
            posicao=data.get('posicao')
        )
        return jsonify({
            "id": nova_figurinha.id,
            "numero": nova_figurinha.numero,
            "posicao": nova_figurinha.posicao
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@figurinha_blueprint.route('/figurinhas', methods=['GET'])
def list_figurinhas():
    figurinhas = list_service.execute()
    
    output = [
        {"id": f.id, "numero": f.numero, "posicao": f.posicao} 
        for f in figurinhas
    ]
    return jsonify(output), 200


@figurinha_blueprint.route('/figurinhas/<int:id>', methods=['GET'])
def get_figurinha(id: int):
    figurinha = get_by_id_service.execute(id)
    
    if not figurinha:
        return jsonify({"error": "Figurinha não encontrada"}), 404
        
    return jsonify({
        "id": figurinha.id,
        "numero": figurinha.numero,
        "posicao": figurinha.posicao
    }), 200


@figurinha_blueprint.route('/figurinhas/<int:id>', methods=['DELETE'])
def delete_figurinha(id: int):
    figurinha = get_by_id_service.execute(id)
    if not figurinha:
        return jsonify({"error": "Figurinha não encontrada"}), 404
        
    delete_service.execute(id)
    return jsonify({"message": "Figurinha deletada com sucesso"}), 200