# Dockerfile

# 1. IMAGEN BASE
# Usamos python:3.9-slim para un tamaño de imagen reducido
FROM python:3.9-slim

# 2. DIRECTORIO DE TRABAJO
WORKDIR /app

# 3. COPIAR DEPENDENCIAS e INSTALAR
# Copiamos solo el archivo de requisitos primero para aprovechar el caché de Docker
COPY requirements.txt .
# Instalar las dependencias de Python (Flask, scikit-learn, Gunicorn, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPIAR ARCHIVOS DE LA APLICACIÓN Y MODELO
# Copiamos la lógica de la API y los archivos del modelo
COPY app.py .
COPY model.joblib .
COPY model_info.joblib .

# 5. EXPONER PUERTO
# Indicar qué puerto escucha la aplicación
EXPOSE 5000

# 6. COMANDO DE EJECUCIÓN
# Usamos Gunicorn para servir la aplicación en producción (app:app -> archivo:instancia)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
