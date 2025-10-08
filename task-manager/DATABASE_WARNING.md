⚠️ **IMPORTANTE: Base de Datos en Vercel**

Este proyecto usa SQLite en memoria para el despliegue en Vercel, lo que significa que:

- ✅ Funciona perfectamente para demostración
- ❌ Los datos se borran cada vez que la función serverless se reinicia
- ❌ No hay persistencia entre sesiones

## Solución Recomendada para Producción

Para una aplicación real con persistencia de datos, debes usar una base de datos externa:

### Opción 1: PostgreSQL con Supabase (Recomendado - GRATIS)

1. Crea una cuenta en [Supabase](https://supabase.com)
2. Crea un nuevo proyecto
3. Ve a Settings > Database > Connection string
4. Copia la URL de conexión
5. En Vercel, agrega la variable de entorno:
   ```
   DATABASE_URL = postgresql://user:password@host:port/database
   ```
6. Actualiza `requirements.txt`:
   ```
   psycopg2-binary>=2.9.9
   ```

### Opción 2: PlanetScale (MySQL)

1. Crea una cuenta en [PlanetScale](https://planetscale.com)
2. Crea una nueva database
3. Obtén la connection string
4. En Vercel:
   ```
   DATABASE_URL = mysql://user:password@host/database
   ```
5. Actualiza `requirements.txt`:
   ```
   pymysql>=1.1.0
   ```

### Opción 3: MongoDB Atlas

1. Crea una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crea un cluster gratuito
3. Obtén la connection string
4. Instala Flask-PyMongo y actualiza tu código

## Cambios Necesarios

Una vez que tengas tu base de datos externa, simplemente:

1. Agrega `DATABASE_URL` en las variables de entorno de Vercel
2. La aplicación detectará automáticamente la URL y la usará
3. Redeploy automático desde GitHub

## Verificar Configuración Actual

Para ver qué base de datos está usando:
- Revisa los logs de Vercel
- La configuración está en `src/config.py`
- En Vercel se usa: `SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///:memory:')`