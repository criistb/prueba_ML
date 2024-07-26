# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al directorio de trabajo
COPY . .

# Cambiar al directorio de la aplicación
WORKDIR /app/api_project

# Exponer el puerto que FastAPI utilizará
EXPOSE 8000

# Comando para ejecutar la aplicación
ENTRYPOINT ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & python app/process_data.py"]

