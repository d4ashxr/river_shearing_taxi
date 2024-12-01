from flask_jwt_extended import create_access_token
from datetime import timedelta
from bcrypt import hashpw, gensalt, checkpw

# Генерация хэша пароля
def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

# Проверка пароля
def check_password(hashed_password, password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Генерация JWT токена
def generate_token(identity):
    return create_access_token(identity=identity, expires_delta=timedelta(days=7))
