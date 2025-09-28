# Dockerfile

# 1. IMAGEN BASE
FROM python:3.9-slim

# CORRECCIÓN: Instalar paquetes del sistema necesarios para construir scikit-learn/numpy
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. DIRECTORIO DE TRABAJO
WORKDIR /app

# 3. COPIAR DEPENDENCIAS e INSTALAR
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPIAR ARCHIVOS DE LA APLICACIÓN Y MODELO
COPY app.py .
COPY model.joblib .
COPY model_info.joblib .

# 5. EXPONER PUERTO
EXPOSE 5000

# 6. COMANDO DE EJECUCIÓN
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
