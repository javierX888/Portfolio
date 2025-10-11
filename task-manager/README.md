# Task Manager 🎯

<div align="center">
  
  ![Task Manager](https://img.shields.io/badge/Flask-3.0+-dc4c3e?style=for-the-badge&logo=flask&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-316192?style=for-the-badge&logo=postgresql&logoColor=white)
  ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
  ![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel&logoColor=white)

  **Sistema avanzado de gestión de tareas con diseño moderno y características profesionales**
  
  🔗 **[Ver Demo en Vivo](https://portfolio-self-ten-9zbsbqm3hp.vercel.app/)**

</div>

---

## 🎨 Diseño Moderno Inspirado en Apps Profesionales

Interfaz elegante con colores vibrantes, efectos glassmorphism, animaciones suaves y un sistema de diseño coherente. El esquema de colores rojo vibrante (#dc4c3e) está inspirado en aplicaciones líderes del mercado como Todoist.

### ✨ Características Visuales

- 🎨 **Diseño vibrante y moderno** con gradientes y efectos glassmorphism
- 🌈 **Sistema de prioridades** con 4 niveles de colores (Baja, Media, Alta, Urgente)
- 📊 **Dashboard de estadísticas** con tarjetas animadas y bordes de colores
- 🎭 **Tema oscuro/claro** con transiciones suaves y paleta optimizada
- ✨ **Animaciones fluidas** en cards, botones y transiciones
- 🎯 **Badges con gradientes** para estados y prioridades
- �️ **Iconos contextuales** para categorías con código de colores

## 🚀 Características Principales

### 👤 **Gestión de Usuarios**
- ✅ **Autenticación completa**: Registro, login seguro con hash de contraseñas
- 👤 **Perfil personalizable**: Sube tu foto desde archivo o URL con compresión automática
- 🔒 **Rutas protegidas**: Sistema de autorización con Flask-Login

### 📝 **Gestión Avanzada de Tareas**
- ✅ **CRUD completo**: Crear, leer, actualizar y eliminar tareas
- 🎯 **4 niveles de prioridad**: Baja (🟢), Media (🔵), Alta (🟡), Urgente (🔴)
- 📊 **4 estados de seguimiento**: Pendiente, En Progreso, Completada, Cancelada
- 🏷️ **6 categorías**: Personal, Trabajo, Estudio, Salud, Compras, Otra
- 📅 **Gestión de fechas**: Inicio, vencimiento con alertas visuales de tareas vencidas
- ⏱️ **Tiempo estimado**: En minutos para mejor planificación
- 🔄 **Tareas recurrentes**: Diaria, semanal, mensual con fecha de finalización
- 📝 **Descripciones detalladas**: Hasta 500 caracteres

### 🔍 **Filtrado y Organización**
- � **Filtros avanzados**: Por estado, prioridad y categoría
- 📊 **Ordenamiento personalizable**: Por fecha, prioridad, creación o título
- 📈 **Dashboard de estadísticas**: Total, en progreso, completadas y vencidas

### 🎨 **Experiencia de Usuario**
- � **100% responsivo**: Optimizado para desktop, tablet y móvil
- 🌓 **Selector de tema**: Claro, oscuro o automático (según sistema)
- ⚡ **Carga rápida**: Serverless functions con Vercel
- 🎭 **Animaciones suaves**: Feedback visual en todas las interacciones
- 🖼️ **Compresión de imágenes**: Pillow optimiza fotos de perfil automáticamente

### 🗄️ **Tecnología Backend**
- 🔒 **Base de datos PostgreSQL**: Persistencia segura en la nube con Neon.tech
- 🚀 **API RESTful**: Endpoints bien estructurados con filtros y estadísticas
- 🔐 **Seguridad**: Hashing de contraseñas, protección CSRF, sesiones seguras
- 📦 **Deployment automatizado**: CI/CD con Vercel

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
- 💼 LinkedIn: [Javier Gacitúa](https://www.linkedin.com/in/javier-gacit%C3%BAa)

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