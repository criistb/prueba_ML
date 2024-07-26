# Proyecto de Predicción y API

## Descripción

Este proyecto consiste en la construcción de un modelo de predicción de demanda para Cementos Argos y la implementación de una API que recibe parámetros, realiza predicciones y devuelve los resultados.

## Estructura del Proyecto

- `api_project/`: Carpeta que contiene los archivos del proyecto API.
  - `app/main.py`: Archivo principal que ejecuta la API usando FastAPI.
  - `app/process_data.py`: Script que procesa los datos recibidos y realiza predicciones.
  - `model/classification_pipeline.pkl`: Modelo entrenado para realizar las predicciones.
  - `requirements.txt`: Archivo con las dependencias del proyecto.
  - `output_data.json`: Archivo JSON con los datos exportados.
  - `input_data.json`: Archivo JSON con los datos con el forecast de Demand.

## Archivos y Funcionalidades

### 1. Datos

- **`dataset_demand_acumulate.csv`**: Datos históricos de demanda de Cementos Argos.
- **`dataset_alpha_betha.csv`**: Datos con variables para la clasificación de Alpha y Beta.
- **`to_predict.csv`**: Datos para predecir la demanda.

### 2. Predicción de Demanda

Se ha entrenado un modelo de regresión para predecir la demanda para los meses de 2022-05, 2022-06 y 2022-07. Los resultados se han guardado en el archivo `input_data.json`. Esto lo entrega el notebook

### 3. API para Predicción

La API se ha construido usando FastAPI y permite realizar las siguientes operaciones:

- **POST `/predict/`**: Recibe un JSON con los datos de entrada y devuelve la clasificación de demanda.

## Ejecución

Abrir el proyecto en la carpeta API_project, crear ambiente virtual, instalar el archivo `requirements.txt`. Luego, activar app en la terminal con el comando `uvicorn main:app --reload`, finalmente en otra terminal ejecutar `python/py app/process_data.py` 
