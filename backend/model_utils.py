import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

soil_encoder = LabelEncoder()

soil_types = ['sandy','clay','silt','peat','chalk','loam']
soil_encoder.fit(soil_types)


def preprocess_df(df: pd.DataFrame):
    df = df.copy()
    if 'soil_type' in df.columns:
        df['soil_type'] = soil_encoder.transform(df['soil_type'])
    return df


def decode_label(label_int, label_encoder):
    return label_encoder.inverse_transform([label_int])[0]
