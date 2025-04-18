# Task Manager

Gestor de tareas personal desarrollado con **Flask**, **Bootstrap 5** y **SQLite**. Permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas de manera sencilla y moderna.

---

## Características

- Registro e inicio de sesión de usuarios
- CRUD de tareas (crear, leer, actualizar, eliminar)
- Interfaz responsiva con Bootstrap 5 y estilos personalizados
- API RESTful para operaciones de tareas
- Autenticación y protección de rutas con Flask-Login
- Base de datos SQLite lista para producción o desarrollo en Docker o local

---

## Instalación

### 1. Clona el repositorio

```sh
git clone https://github.com/javierX888/Portfolio.git
cd task-manager
```

### 2. Variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
SECRET_KEY=tu_clave_secreta
```

---

## Ejecución con Docker (recomendado)

Asegúrate de tener Docker y Docker Compose instalados.

```sh
docker-compose up --build
```

La app estará disponible en [http://localhost:5000](http://localhost:5000)

---

## Ejecución sin Docker (modo local)

1. Crea un entorno virtual e instala dependencias:

    ```sh
    python -m venv venv
    venv\Scripts\activate  # En Windows
    # source venv/bin/activate  # En Linux/Mac
    pip install -r requirements.txt
    ```

2. Crea la base de datos manualmente (solo la primera vez):

    ```sh
    python
    >>> from src import create_app, db
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()
    ...
    >>> exit()
    ```

3. Exporta la variable de entorno y ejecuta la app:

    ```sh
    set FLASK_APP=src  # En Windows
    # export FLASK_APP=src  # En Linux/Mac
    flask run
    ```

La app estará disponible en [http://localhost:5000](http://localhost:5000)

---

## Estructura del proyecto

```
src/
  auth/           # Módulo de autenticación
  tasks/          # Módulo de tareas
  static/         # Archivos estáticos (CSS, JS)
  templates/      # Plantillas HTML
  models.py       # Modelos de base de datos
  config.py       # Configuración de la app
  __init__.py     # Inicialización de Flask
```

---

## Personalización

- Los colores y estilos se pueden modificar en `src/static/css/styles.css`.
- Las plantillas HTML están en `src/templates/`.

---

## Licencia

MIT

---

## Autor

Desarrollado por [Tu Nombre o Usuario de GitHub]