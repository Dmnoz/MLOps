# API de Clasificación de Cáncer de Mama

🤖 MLOps Pipeline: Del Desarrollo a la Producción

🌟 Visión General
Este repositorio contiene un template y una demostración de un pipeline de MLOps (Machine Learning Operations) de principio a fin. El objetivo principal es mostrar cómo automatizar, reproducir y monitorear el ciclo de vida completo de un modelo de Machine Learning, desde la ingesta de datos y el entrenamiento, hasta el deployment y la inferencia.

Este proyecto ejemplifica la aplicación de las mejores prácticas de DevOps al mundo del Machine Learning, garantizando la confiabilidad y escalabilidad de los modelos en entornos de producción.

🚀 Características Clave
Integración Continua (CI): Uso de GitHub Actions para pruebas automáticas y validación del código.
Entrega Continua (CD): Deployment automatizado del modelo entrenado como un servicio de API REST (usando Flask o FastAPI).
Seguimiento de Experimentos: Integración con MLflow para registrar modelos, métricas, parámetros e historial de runs.
Versionamiento de Datos y Modelos: Implementación de DVC (Data Version Control) para manejar grandes datasets fuera del repositorio Git.
Contenerización: Uso de Docker para asegurar la reproducibilidad del entorno de entrenamiento e inferencia.
Estructura Modular: Diseño basado en módulos para separar las tareas de data ingestion, data processing y model training.
