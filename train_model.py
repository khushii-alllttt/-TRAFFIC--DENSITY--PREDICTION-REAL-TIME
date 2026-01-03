import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
import os

df = pd.read_csv("traffic.csv")

X = df[['vehicles', 'time', 'weather', 'road_type']]
y = df['density']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# auto create folder
os.makedirs("models", exist_ok=True)

pickle.dump(model, open("models/traffic_model.pkl", "wb"))

print("✅ Model trained and saved successfully")
