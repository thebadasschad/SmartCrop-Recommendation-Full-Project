from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from model_utils import preprocess_df

app = FastAPI(title='SmartCrop API')

MODEL_PATH = 'backend/model.joblib'
MODEL_OBJ = None

class PredictRequest(BaseModel):
    pH: float
    N: float
    P: float
    K: float
    avg_temp: float
    rainfall: float
    humidity: float
    altitude: float
    soil_type: str = 'loam'

@app.on_event('startup')
def load_model():
    global MODEL_OBJ
    MODEL_OBJ = joblib.load(MODEL_PATH)

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/predict')
def predict(req: PredictRequest):
    df = pd.DataFrame([req.dict()])
    X = preprocess_df(df)
    clf = MODEL_OBJ['model']
    pred = clf.predict(X)[0]
    label_encoder = MODEL_OBJ.get('label_encoder', None)
    if label_encoder is not None:
        crop_name = label_encoder.inverse_transform([int(pred)])[0]
        return {'predicted_crop': crop_name}
    return {'predicted_label_int': int(pred)}
