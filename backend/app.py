from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from db import db, init_db
from config import Config
from flask_cors import CORS

# Включаем CORS для всего приложения

# Или включаем CORS только для нужных эндпоинтов:
# CORS(auth_bp)


bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Инициализация расширений
    init_db(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Регистрация блюпринтов
    from auth.routes import auth_bp
    from rides.routes import rides_bp
    from routes.routes import routes_bp
    from piers.routes import piers_bp
    from faq.routes import faq_bp
    from maps.routes import maps_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(rides_bp, url_prefix='/rides')
    app.register_blueprint(routes_bp, url_prefix='/routes')
    app.register_blueprint(piers_bp, url_prefix='/piers')
    app.register_blueprint(faq_bp, url_prefix='/faq')
    app.register_blueprint(maps_bp, url_prefix='/maps')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Создание таблиц при старте
    app.run(debug=True)
