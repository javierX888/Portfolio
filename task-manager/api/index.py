import sys
import os

# Agregar el directorio src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from src import create_app
    from src.models import db
    
    # Crear la aplicación Flask
    app = create_app()
    
    # Configurar la base de datos para Vercel (usar SQLite en memoria)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Crear las tablas en el contexto de la aplicación
    with app.app_context():
        db.create_all()
        
except ImportError as e:
    print(f"Error importing modules: {e}")
    # Crear una aplicación básica en caso de error
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Hello from Vercel!'

# Para desarrollo local y deployment en Vercel
if __name__ == '__main__':
    app.run(debug=True)