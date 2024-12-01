from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from auth.models import User
from auth.utils import hash_password, check_password
from db import db

auth_bp = Blueprint('auth', __name__)


# Регистрация
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name')
    role = data.get('role', 'passenger')  # По умолчанию "пассажир"

    if role not in ['passenger', 'driver']:
        return jsonify({"error": "Invalid role"}), 400

    if not email or not password or not full_name:
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_password = hash_password(password)
    new_user = User(email=email, password=hashed_password, full_name=full_name, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "role": role}), 201


# Вход
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Генерация токена
    token = create_access_token(identity={"id": user.id, "email": user.email, "role": user.role})

    # Возвращаем токен без использования сессии
    return jsonify({"access_token": token,
                    "role": user.role,
                    "email": user.email,
                    "full_name": user.full_name,
                    "payment_method": user.payment_method
                    }), 200


# Профиль
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()  # Проверка наличия токена в заголовке запроса
def get_profile():
    try:
        user_identity = get_jwt_identity()  # Получаем информацию о пользователе из токена
        user = User.query.get(user_identity['id'])  # Запрос пользователя по ID
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "payment_method": user.payment_method
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Выход (по сути, его можно удалить, так как сессии нет)
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # С токеном, хранящимся в заголовке, нет необходимости в сессиях
    return jsonify({"message": "Successfully logged out"}), 200
