from flask import jsonify
from . import piers_bp

@piers_bp.route('/', methods=['GET'])
def get_piers():
    # Возвращает список причалов
    pass

@piers_bp.route('/<int:pier_id>', methods=['GET'])
def get_pier_details(pier_id):
    # Возвращает детали причала
    pass
