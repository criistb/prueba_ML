# Proyecto de Predicción y API

## Descripción

Este proyecto consiste en la construcción de un modelo de predicción de demanda para Cementos Argos y la implementación de una API que recibe parámetros, realiza predicciones y devuelve los resultados.

## Estructura del Proyecto

- `PRUEBA_TECNICA/`: Carpeta que contiene los archivos del la prueba.
  - `api_project/`: Carpeta que contiene los archivos del proyecto API.
    - `app/main.py`: Archivo principal que ejecuta la API usando FastAPI.
    - `app/process_data.py`: Script que procesa los datos recibidos y realiza predicciones.
    - `model/classification_pipeline.pkl`: Modelo entrenado para realizar las predicciones.
    - `output_data.json`: Archivo JSON con los datos exportados.
    - `input_data.json`: Archivo JSON con los datos con el forecast de Demand.
  - `bds/`: Carpeta que contiene las fuentes de datos.
  - `results/`: Carpeta que contiene los resultados del jupyter notebook.
  - `PruebaTecnica.ipynb`: Jupyter notebook con la solucion de la prueba, contiene el forecast y la prediccion de la clase
  - `requirements.txt`: Archivo con las dependencias del proyecto.

## Archivos y Funcionalidades

### 1. Datos

- **`dataset_demand_acumulate.csv`**: Datos históricos de demanda de Cementos Argos.
- **`dataset_alpha_betha.csv`**: Datos con variables para la clasificación de Alpha y Beta.
- **`to_predict.csv`**: Datos para predecir la demanda.

### 2. Predicción de Demanda

Se ha entrenado un modelo para predecir la demanda para los meses de 2022-05, 2022-06 y 2022-07. Los resultados del archivo `to_predict.csv` se han guardado en el archivo `input_data.json`. Esto lo entrega el notebook y es necesario para la posterior ejecucucion de la aplicación que realiza la clasificación. La ejecución del notebook tambien arroja en la carpeta results, los resultados de la clasificación hecha directamente asi como metricas de los modelos y finalmente el pipeline que usará la aplicación.

### 3. API para Predicción

La API se ha construido usando FastAPI y permite realizar las siguientes operaciones:

- **POST `/predict/`**: Recibe un JSON con los datos de entrada y devuelve la clasificación de demanda

## Ejecución

Clonar el repositorio en local, crear ambiente virtual, activarlo e instalar el `requirements.txt`. Luego ejecutar completamente el Notebook `PruebaTecnica.ipynb`. Posteriormente, ir a la carpeta `api_project` y activar app en la terminal con el comando `uvicorn app.main:app --reload`,(toma unos segundos, esperar a que muestre "aplication startup complete") finalmente en otra terminal ejecutar `(python/py) api_project/app/process_data.py`. Esto entregará el json con la clasificación

### Dockerfile

La funcionalidad fue intentada para añadirse pero requiere ajustes, por el momento no usarla.
