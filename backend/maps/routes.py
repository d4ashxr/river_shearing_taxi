from flask import jsonify, request
from . import maps_bp
from .utils import nearest_docks, docks

@maps_bp.route('/location', methods=['GET'])
def get_location():
    # Возвращает текущую геолокацию пользователя
    return 'nice'

@maps_bp.route('/routes', methods=['GET'])
def get_map_routes():
    # Возвращает маршруты для карты
    pass

@maps_bp.route('/allpiers', methods=['GET'])
def get_all_docks():
    # Возвращаем список всех причалов
    response = [{'name': dock['name'], 'coordinates': dock['coordinates']} for dock in docks]
    return jsonify(response), 200


@maps_bp.route('/nearpier', methods=['GET'])
def get_near_pier():
    try:
        # Получаем координаты из параметров запроса
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))
        print(x, y)
        # Проверяем, что координаты переданы корректно
        if not x or not y:
            return jsonify({'error': 'Координаты x и y обязательны'}), 400

        # Находим ближайшие причалы
        top_docks = nearest_docks((x, y))

        # Формируем ответ
        response = [{'name': dock['name'], 'coordinates': dock['coordinates'], 'distance': round(dock['distance'], 2)} for dock in top_docks]

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': 'Ошибка'}), 400


