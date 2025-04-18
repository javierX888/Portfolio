from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')  # Asegúrate de tener este archivo de configuración
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Registrar blueprints
    from src.auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    from src.tasks.routes import tasks_bp
    app.register_blueprint(tasks_bp)  # Sin url_prefix

    @login_manager.user_loader
    def load_user(user_id):
        from src.models import User
        return User.query.get(int(user_id))
    
    return app