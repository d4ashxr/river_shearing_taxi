from flask import jsonify
from . import routes_bp

@routes_bp.route('/', methods=['GET'])
def get_routes():
    # Возвращает список маршрутов
    return 'cool'

@routes_bp.route('/<int:route_id>', methods=['GET'])
def get_route_details(route_id):
    # Возвращает детали маршрута
    pass
