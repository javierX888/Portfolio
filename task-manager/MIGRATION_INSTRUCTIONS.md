# 🔧 Migración de Base de Datos - Profile Picture

## ⚠️ IMPORTANTE: Debes ejecutar esta migración UNA VEZ

El campo `profile_picture` en la base de datos está limitado a 200 caracteres, pero las imágenes base64 pueden ser mucho más grandes.

---

## 📋 Pasos para Aplicar la Migración:

### 1. Abre Neon Console
Ve a: **https://console.neon.tech/**

### 2. Selecciona tu Proyecto
- Haz clic en tu proyecto **"task-manager"**

### 3. Abre el SQL Editor
- En el menú lateral izquierdo, haz clic en **"SQL Editor"**
- O ve directamente a: https://console.neon.tech/app/projects/quiet-feather-53348450/sql-editor

### 4. Copia y Pega el SQL
Copia TODO el contenido del archivo `migration.sql` o usa este código:

```sql
ALTER TABLE "user" ALTER COLUMN profile_picture TYPE TEXT;
```

### 5. Ejecuta la Migración
- Haz clic en el botón **"Run"** (▶️) o presiona `Ctrl + Enter`
- Deberías ver un mensaje: **"Success"** o **"ALTER TABLE"**

### 6. Verifica el Cambio (Opcional)
Ejecuta esta consulta para verificar:

```sql
SELECT column_name, data_type, character_maximum_length 
FROM information_schema.columns 
WHERE table_name = 'user' AND column_name = 'profile_picture';
```

Debería mostrar:
- `data_type`: **text**
- `character_maximum_length`: **NULL** (sin límite)

---

## ✅ Después de la Migración

1. **Recarga tu aplicación** en Vercel
2. **Ve a tu perfil** en la app
3. **Sube tu foto** nuevamente
4. **Debería funcionar sin errores** 🎉

---

## 🐛 Solución de Problemas

### Si ves error "relation does not exist"
- Verifica que estés conectado a la base de datos correcta
- Verifica que la tabla se llame exactamente `user` (en minúsculas)

### Si ya aplicaste la migración
- No pasa nada si la ejecutas de nuevo
- PostgreSQL simplemente dirá que ya es tipo TEXT

---

## 📞 ¿Necesitas Ayuda?

Si tienes problemas, verifica:
1. ✅ Que estés en el proyecto correcto de Neon
2. ✅ Que la conexión a la base de datos funcione
3. ✅ Que hayas copiado el SQL completo

---

**Última actualización:** 8 de Octubre 2025
