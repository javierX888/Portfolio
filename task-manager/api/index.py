import sys
import os

# Agregar el directorio padre al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Importar la aplicación Flask completa
from src import create_app
from src.models import db

# Crear la aplicación Flask completa con todas las rutas
app = create_app()

# Inicializar la base de datos
with app.app_context():
    try:
        db.create_all()
        print("✅ Base de datos inicializada correctamente")
    except Exception as e:
        print(f"⚠️ Error inicializando base de datos: {e}")

# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)