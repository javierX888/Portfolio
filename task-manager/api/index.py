import sys
import os
from flask import Flask

# Agregar el directorio padre al path para importar módulos
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, '..')
sys.path.insert(0, parent_dir)

# Inicializar la aplicación Flask
app = Flask(__name__)

try:
    # Intentar importar y configurar la aplicación completa
    from src import create_app
    from src.models import db
    
    # Crear la aplicación Flask completa
    full_app = create_app()
    
    # Configurar la aplicación para Vercel
    app = full_app
    
    # Crear las tablas en el contexto de la aplicación
    with app.app_context():
        db.create_all()
        
    print("✅ Aplicación Flask configurada correctamente")
    
except Exception as e:
    print(f"❌ Error configurando aplicación: {e}")
    
    # Crear rutas básicas como fallback
    @app.route('/')
    def hello():
        return f'''
        <h1>🚀 Flask en Vercel</h1>
        <p><strong>Estado:</strong> Ejecutándose pero con errores de importación</p>
        <p><strong>Error:</strong> {str(e)}</p>
        <p><strong>Directorio actual:</strong> {os.getcwd()}</p>
        <p><strong>Python path:</strong> {sys.path[:3]}</p>
        '''
    
    @app.route('/health')
    def health():
        return {'status': 'ok', 'message': 'Flask app is running on Vercel'}

# Esta línea es importante para Vercel
if __name__ == '__main__':
    app.run(debug=False)