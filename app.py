# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# --- Configuración y Carga del Modelo ---
MODEL_PATH = 'model.joblib'
MODEL_INFO_PATH = 'model_info.joblib'

try:
    # Carga el modelo de Machine Learning
    model = joblib.load(MODEL_PATH)
    model_info = joblib.load(MODEL_INFO_PATH)
    
    NUM_FEATURES = model_info['num_features']
    TARGET_NAMES = model_info['target_names']
    
    print(f"✅ Modelo cargado exitosamente. Esperando {NUM_FEATURES} características.")
    
except Exception as e:
    # Maneja el error si los archivos del modelo no se encuentran
    print(f"Error al cargar el modelo: {e}. Usando valores por defecto.")
    NUM_FEATURES = 30 
    TARGET_NAMES = ['malignant', 'benign']

# Inicializar la aplicación Flask
app = Flask(__name__)

# --- ENDPOINT 1: Mensaje de Bienvenida (GET) ---
@app.route('/', methods=['GET'])
def home():
    """Ruta para verificar el estado del servicio y sus requisitos."""
    return jsonify({
        "status": "OK",
        "service": "API de Clasificación de Cáncer de Mama",
        "predict_endpoint": "/predict (POST)",
        "features_required": NUM_FEATURES,
        "classes": TARGET_NAMES
    })

# --- ENDPOINT 2: Predicción (POST) ---
@app.route('/predict', methods=['POST'])
def predict():
    """
    Recibe un cuerpo JSON con una lista de características y devuelve una predicción.
    Formato JSON esperado: {"features": [v1, v2, v3, ...]}
    """
    data = request.get_json(silent=True)

    # 1. Manejo de Errores: Solicitud mal formada o clave 'features' faltante
    if not data or 'features' not in data:
        return jsonify({
            "error": "BAD_REQUEST",
            "message": "Se espera un cuerpo JSON con la clave 'features': [v1, v2, ...]"
        }), 400

    features = data.get('features')

    # 2. Manejo de Errores: Número incorrecto de características
    if not isinstance(features, list) or len(features) != NUM_FEATURES:
        return jsonify({
            "error": "VALIDATION_ERROR",
            "message": f"Se esperaba una lista de {NUM_FEATURES} valores. Se recibieron {len(features)}."
        }), 400
    
    # 3. Predicción
    try:
        # Convierte la lista de características en un array 2D para el modelo
        input_array = np.array([features])
        prediction_index = model.predict(input_array)[0]
        
        # Obtiene el nombre de la clase predicha
        predicted_class_name = TARGET_NAMES[prediction_index]

    except Exception as e:
        # 4. Manejo de Errores: Error interno
        return jsonify({
            "error": "INTERNAL_SERVER_ERROR",
            "message": f"Error al realizar la predicción: {str(e)}"
        }), 500

    # 5. Respuesta Exitosa
    return jsonify({
        "prediction": predicted_class_name,
        "class_index": int(prediction_index)
    }), 200

# Gunicorn usará 'app:app' para iniciar.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
