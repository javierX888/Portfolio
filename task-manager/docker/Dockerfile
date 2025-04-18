FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    dos2unix \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de datos
RUN mkdir -p /data

# Copiar todo el proyecto
COPY . .

# Asegurarnos de que entrypoint tenga formato Unix y permiso de ejecución
RUN sed -i 's/\r$//' entrypoint.sh && \
    chmod +x entrypoint.sh

# Asegurarnos de que entrypoint.sh tenga permiso de ejecución
RUN chmod +x /app/entrypoint.sh

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Usar shell como entrypoint para asegurarnos de que funcione correctamente
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]