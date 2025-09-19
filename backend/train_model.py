import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from model_utils import soil_encoder

# Dummy training data
data = {
    'pH': [6.5,5.8,7.0,6.0,6.2],
    'N': [300,200,100,150,250],
    'P': [40,35,20,25,30],
    'K': [200,100,150,120,180],
    'avg_temp': [25,28,22,30,24],
    'rainfall': [800,1200,400,600,700],
    'humidity': [60,70,55,65,80],
    'altitude': [300,500,100,50,400],
    'soil_type': ['loam','clay','sandy','silt','loam'],
    'crop': ['wheat','rice','maize','millet','barley']
}

df = pd.DataFrame(data)
df['soil_type'] = soil_encoder.transform(df['soil_type'])

X = df.drop('crop', axis=1)
y = df['crop']

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y_enc = label_encoder.fit_transform(y)

X_train,X_test,y_train,y_test = train_test_split(X,y_enc,test_size=0.2,random_state=42)
clf = RandomForestClassifier(n_estimators=100,random_state=42)
clf.fit(X_train,y_train)

# Save model with encoders
joblib.dump({'model':clf,'label_encoder':label_encoder,'soil_encoder':soil_encoder}, 'backend/model.joblib')
print("Model trained and saved to backend/model.joblib")
