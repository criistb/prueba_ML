# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Intentar cargar el modelo
try:
    model = joblib.load('model/classification_pipeline.pkl')
    print("Modelo cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")

# Definir el esquema del JSON de entrada
class PredictionRequest(BaseModel):
    autoID: str
    SeniorCity: str
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float
    Demand: float

# Definir el esquema del JSON de salida
class PredictionResponse(BaseModel):
    classification: str

@app.post("/predict/", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Convertir el JSON de entrada en un DataFrame
    input_data = pd.DataFrame([request.dict()])
    
    # Asegurarse de que el DataFrame tenga todas las columnas esperadas
    expected_columns = [
        'autoID', 'SeniorCity', 'Partner', 'Dependents', 'Service1', 'Service2',
        'Security', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'Charges', 'Demand'
    ]
    
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = None  # Agregar columnas faltantes con valores nulos
    
    # Realizar la predicción
    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error en la predicción")
    
    return PredictionResponse(classification=prediction)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
