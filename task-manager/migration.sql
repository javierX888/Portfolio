-- MIGRACIÓN: Actualizar campo profile_picture para soportar imágenes base64
-- Fecha: 8 de Octubre 2025
-- Base de datos: PostgreSQL (Neon)

-- Cambiar el tipo de columna de VARCHAR(200) a TEXT
ALTER TABLE "user" ALTER COLUMN profile_picture TYPE TEXT;

-- Verificar que el cambio se aplicó correctamente
SELECT 
    column_name, 
    data_type, 
    character_maximum_length 
FROM information_schema.columns 
WHERE table_name = 'user' 
  AND column_name = 'profile_picture';

-- El resultado debería mostrar:
-- column_name      | data_type | character_maximum_length
-- profile_picture  | text      | NULL
