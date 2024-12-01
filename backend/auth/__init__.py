def init_app(app):
    from auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')