# Despliegue en Vercel - Guía Paso a Paso

## Configuración del Proyecto

Este proyecto Flask ha sido configurado para desplegarse en Vercel usando funciones serverless.

### Archivos de Configuración

1. **`vercel.json`** - Configuración principal de Vercel
2. **`api/index.py`** - Punto de entrada de la aplicación Flask
3. **`requirements.txt`** - Dependencias de Python

## Pasos para Desplegar

### 1. Configurar Variables de Entorno en Vercel

En el dashboard de Vercel, ve a tu proyecto > Settings > Environment Variables y agrega:

```
SECRET_KEY = "tu_clave_secreta_muy_segura_para_produccion"
VERCEL_ENV = "production"
```

### 2. Configuración del Root Directory

- **Root Directory**: `task-manager`
- **Framework Preset**: Other
- **Build Command**: (dejar vacío)
- **Output Directory**: (dejar vacío)

### 3. Desplegar

1. Conecta tu repositorio GitHub a Vercel
2. Selecciona la carpeta `task-manager` como Root Directory
3. Configura las variables de entorno
4. Haz clic en "Deploy"

## Consideraciones Importantes

### Base de Datos

- **Desarrollo**: SQLite local
- **Producción (Vercel)**: SQLite en memoria (se reinicia en cada invocación)
- **Recomendado para producción**: Usar una base de datos externa como:
  - PostgreSQL (Supabase, Neon, etc.)
  - MySQL (PlanetScale, etc.)
  - MongoDB Atlas

### Limitaciones de Vercel con SQLite

- Los datos se pierden entre despliegues
- No hay persistencia de datos
- Para una aplicación real, usa una base de datos externa

### Configurar Base de Datos Externa (Opcional)

1. Crea una cuenta en un proveedor de base de datos (ejemplo: Supabase)
2. Obtén la URL de conexión
3. Agrega la variable de entorno en Vercel:
   ```
   DATABASE_URL = "postgresql://user:password@host:port/database"
   ```

## Archivos Estáticos

Los archivos CSS y JavaScript en `src/static/` se servirán correctamente gracias a la configuración en `vercel.json`.

## Solución de Problemas

### Error de Importación

Si ves errores de importación, verifica que:
1. El Root Directory esté configurado como `task-manager`
2. Todas las dependencias estén en `requirements.txt`
3. Las rutas de importación en `api/index.py` sean correctas

### Error de Base de Datos

Si hay errores relacionados con la base de datos:
1. Verifica que `VERCEL_ENV` esté configurado
2. Considera usar una base de datos externa para persistencia

### Logs de Vercel

Para ver los logs de despliegue:
1. Ve a tu proyecto en Vercel
2. Haz clic en "Functions"
3. Selecciona la función y ve a "Logs"

## Comandos Útiles

```bash
# Instalar dependencias localmente
pip install -r requirements.txt

# Ejecutar localmente
python api/index.py

# Verificar que todo funciona
python -c "from src import create_app; app = create_app(); print('OK')"
```

## Estructura Final del Proyecto

```
task-manager/
├── vercel.json              # Configuración de Vercel
├── .env.example            # Variables de entorno de ejemplo
├── requirements.txt        # Dependencias
├── api/
│   └── index.py           # Punto de entrada para Vercel
└── src/                   # Código de la aplicación Flask
    ├── __init__.py
    ├── config.py          # Configuración actualizada
    ├── models.py
    ├── auth/
    ├── tasks/
    ├── static/
    └── templates/
```