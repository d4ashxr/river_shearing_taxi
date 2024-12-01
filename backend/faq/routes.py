from flask import jsonify
from . import faq_bp

@faq_bp.route('/', methods=['GET'])
def get_faq():
    # Возвращает список вопросов
    pass

@faq_bp.route('/search', methods=['GET'])
def search_faq():
    # Поиск вопросов
    pass
