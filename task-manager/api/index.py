from flask import Flask

# Crear aplicación Flask simple
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Manager - Vercel</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .status { background: #d4edda; color: #155724; padding: 10px; border-radius: 5px; margin: 20px 0; }
            .links { margin: 20px 0; }
            .links a { display: inline-block; margin: 10px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Task Manager</h1>
            <div class="status">
                ✅ Aplicación Flask desplegada exitosamente en Vercel
            </div>
            <p>Esta es una aplicación de gestión de tareas construida con Flask y desplegada en Vercel.</p>
            <div class="links">
                <a href="/health">Estado de Salud</a>
                <a href="/about">Acerca de</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {
        'status': 'ok',
        'message': 'Flask app running successfully on Vercel',
        'version': '1.0.0'
    }

@app.route('/about')
def about():
    return '''
    <h1>Acerca del Proyecto</h1>
    <p>Task Manager - Una aplicación web para gestión de tareas</p>
    <p><strong>Tecnologías:</strong> Flask, Python, Vercel</p>
    <p><a href="/">← Volver al inicio</a></p>
    '''

# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)