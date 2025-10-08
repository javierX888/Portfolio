import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key-for-vercel-deployment')
    
    # Detectar si estamos en Vercel (automático)
    # VERCEL_ENV es establecida automáticamente por Vercel
    is_vercel = os.getenv('VERCEL') or os.getenv('VERCEL_ENV')
    
    if is_vercel:
        # En Vercel, usar base de datos en memoria o externa
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
    else:
        # Para desarrollo local
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tasks.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False