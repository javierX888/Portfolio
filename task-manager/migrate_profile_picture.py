"""
Script de migración para actualizar el campo profile_picture a TEXT
Este script debe ejecutarse UNA VEZ en la base de datos de Neon
"""

SQL_MIGRATION = """
-- Actualizar el campo profile_picture de VARCHAR(200) a TEXT
ALTER TABLE "user" ALTER COLUMN profile_picture TYPE TEXT;

-- Verificar el cambio
SELECT column_name, data_type, character_maximum_length 
FROM information_schema.columns 
WHERE table_name = 'user' AND column_name = 'profile_picture';
"""

print("=" * 80)
print("MIGRACIÓN DE BASE DE DATOS - TASK MANAGER")
print("=" * 80)
print("\nPara aplicar esta migración en tu base de datos Neon:")
print("\n1. Ve a: https://console.neon.tech/")
print("2. Selecciona tu proyecto 'task-manager'")
print("3. Haz clic en 'SQL Editor' en el menú lateral")
print("4. Copia y pega el siguiente SQL:\n")
print("-" * 80)
print(SQL_MIGRATION)
print("-" * 80)
print("\n5. Haz clic en 'Run' para ejecutar la migración")
print("6. Deberías ver un mensaje de éxito")
print("\n" + "=" * 80)
print("IMPORTANTE: Esta migración solo debe ejecutarse UNA VEZ")
print("=" * 80)
