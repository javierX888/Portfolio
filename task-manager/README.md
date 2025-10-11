# Task Manager 🎯

Gestor de tareas personal desarrollado con **Flask**, **Bootstrap 5** y **PostgreSQL**. Permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas de manera sencilla y moderna.

🔗 **[Ver Demo en Vivo](https://portfolio-self-ten-9zbsbqm3hp.vercel.app/)**

---

## ✨ Características

- ✅ **Autenticación completa**: Registro, login y gestión de perfiles de usuario
- 📝 **CRUD de tareas**: Crear, leer, actualizar y eliminar tareas
- 👤 **Perfil personalizable**: Sube tu foto de perfil desde archivo o URL
- 🎨 **Selector de tema**: Cambio entre modo claro, oscuro o automático (sistema)
- 📱 **Interfaz responsiva**: Diseño optimizado con Bootstrap 5
- 🔒 **Rutas protegidas**: Autenticación y autorización con Flask-Login
- 🗄️ **Base de datos PostgreSQL**: Persistencia en la nube con Neon.tech
- 🚀 **Deployment en Vercel**: Producción lista con serverless functions
- 🖼️ **Compresión de imágenes**: Optimización automática de fotos de perfil con Pillow

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

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.0+, SQLAlchemy, Flask-Login, Flask-WTF
- **Frontend**: Bootstrap 5, Vanilla JavaScript, Font Awesome
- **Base de datos**: PostgreSQL (Neon.tech)
- **Deployment**: Vercel Serverless Functions
- **Procesamiento de imágenes**: Pillow
- **Autenticación**: Flask-Login con sesiones

---

## 📸 Screenshots

_(Agrega capturas de pantalla de tu aplicación aquí)_

---

## 🚀 Roadmap

- [ ] Filtros avanzados para tareas (por fecha, prioridad)
- [ ] Notificaciones por correo
- [ ] Compartir tareas con otros usuarios
- [ ] Categorías y etiquetas para tareas
- [ ] Exportar tareas a PDF/CSV

---

## 📄 Licencia

MIT License - siéntete libre de usar este proyecto para aprender o como base para tus propios proyectos.

---

## 👨‍💻 Desarrollado por

**Javier Gacitúa**

- 🔗 GitHub: [@javierX888](https://github.com/javierX888)
- 📂 Proyecto: [Portfolio - Task Manager](https://github.com/javierX888/Portfolio)
- 💼 LinkedIn: [Javier Gacitúa](https://www.linkedin.com/in/javier-gacitua/)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún bug o tienes sugerencias:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: Amazing Feature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

<div align="center">
  <p>⭐ Si te gustó este proyecto, dale una estrella en GitHub ⭐</p>
  <p>Desarrollado con ❤️ usando Flask, Bootstrap 5 y PostgreSQL</p>
  <p>© 2025 Javier Gacitúa. Todos los derechos reservados.</p>
</div>