from flask import Blueprint, jsonify
from app.services.greeting_service import GreetingService

health_bp = Blueprint('health', __name__, url_prefix='/')


@health_bp.route('health', methods=['GET'])
def health():
    service = GreetingService()
    return jsonify({
        'status': 'ok',
        'message': service.greet('world')
    })
