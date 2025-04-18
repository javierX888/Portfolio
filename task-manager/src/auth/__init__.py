from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instancia separada
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    
    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Registrar blueprints
    from src.auth import auth_bp  # Se usa el blueprint ya definido
    from src.tasks.routes import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    # Cargar user loader dentro del contexto
    @login_manager.user_loader
    def load_user(user_id):
        from src.models import User
        return User.query.get(int(user_id))
    
    # Renderizar plantilla de login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        from src.auth.forms import LoginForm
        form = LoginForm()
        return render_template('login.html', form=form)
    
    return app

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates/auth')

from . import routes