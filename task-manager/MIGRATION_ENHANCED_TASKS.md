# 📋 Instrucciones de Migración - Tareas Mejoradas

## 🎯 Objetivo
Agregar campos avanzados al modelo de tareas sin perder datos existentes.

## 🔄 Pasos para Migrar la Base de Datos

### 1. **Accede a tu consola de Neon**
   - Ve a https://console.neon.tech/
   - Selecciona tu proyecto: `neondb`
   - Ve a la pestaña **SQL Editor**

### 2. **Ejecuta el script de migración**
   - Abre el archivo `migration_enhanced_tasks.sql`
   - Copia TODO el contenido
   - Pégalo en el SQL Editor de Neon
   - Haz clic en **Run** para ejecutar

### 3. **Verifica los cambios**
   El script te mostrará todas las columnas de la tabla `task` al final.

   Deberías ver las nuevas columnas:
   - ✅ `priority` (INTEGER)
   - ✅ `status` (VARCHAR)
   - ✅ `category` (VARCHAR)
   - ✅ `start_date` (TIMESTAMP)
   - ✅ `due_date` (TIMESTAMP)
   - ✅ `completed_at` (TIMESTAMP)
   - ✅ `estimated_time` (INTEGER)
   - ✅ `is_recurring` (BOOLEAN)
   - ✅ `recurrence_pattern` (VARCHAR)
   - ✅ `recurrence_end_date` (TIMESTAMP)
   - ✅ `recurrence_days` (VARCHAR)

### 4. **Qué hace el script automáticamente**
   - ✅ Agrega todas las columnas nuevas
   - ✅ Establece valores por defecto para tareas existentes
   - ✅ Actualiza tareas completadas con status='completed'
   - ✅ Crea índices para mejorar el rendimiento
   - ✅ **NO elimina ni modifica datos existentes**

## 🚀 Después de la Migración

1. **Actualiza el código localmente:**
   ```bash
   git pull origin main
   ```

2. **Vercel se actualizará automáticamente** con el nuevo deployment

3. **Prueba las nuevas funcionalidades:**
   - Crear tareas con prioridad
   - Establecer fechas de vencimiento
   - Asignar categorías
   - Configurar tareas recurrentes

## 📊 Nuevos Campos Disponibles

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `priority` | 1-4 | Baja(1), Media(2), Alta(3), Urgente(4) |
| `status` | String | pending, in_progress, completed, cancelled |
| `category` | String | personal, work, study, health, other |
| `start_date` | DateTime | Fecha de inicio de la tarea |
| `due_date` | DateTime | Fecha límite de entrega |
| `completed_at` | DateTime | Cuándo se completó |
| `estimated_time` | Integer | Tiempo estimado en minutos |
| `is_recurring` | Boolean | Si la tarea se repite |
| `recurrence_pattern` | String | daily, weekly, monthly |
| `recurrence_end_date` | DateTime | Hasta cuándo se repite |
| `recurrence_days` | String | Días de semana (ej: "1,3,5") |

## ⚠️ Notas Importantes

- ✅ **Es seguro ejecutar este script** - no elimina datos
- ✅ Puedes ejecutarlo múltiples veces sin problemas (usa `IF NOT EXISTS`)
- ✅ Las tareas existentes mantendrán sus títulos y estados
- ✅ Los valores por defecto se aplicarán automáticamente

## 🐛 ¿Problemas?

Si encuentras algún error:
1. Copia el mensaje de error
2. Verifica que estés en la base de datos correcta
3. Consulta con el equipo de desarrollo

---

**¿Listo para ejecutar? Adelante! 🚀**
