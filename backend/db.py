from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Инициализация SQLAlchemy
db = SQLAlchemy()

# Функция для подключения базы данных
def init_db(app):
    db.init_app(app)
    Migrate(app, db)  # Добавляем поддержку миграций
