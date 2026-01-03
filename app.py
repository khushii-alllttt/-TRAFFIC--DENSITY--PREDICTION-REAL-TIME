import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="Traffic Density Prediction", layout="centered")

st.title("🚦 Traffic Density Prediction System")
st.write("Predict traffic density using Machine Learning")

# Check model
if not os.path.exists("models/traffic_model.pkl"):
    st.error("❌ Model file not found. Train model first.")
    st.stop()

# Load model
model = pickle.load(open("models/traffic_model.pkl", "rb"))

# Inputs
vehicles = st.number_input("Number of Vehicles", 0, 500, 50)
time = st.slider("Time of Day (Hour)", 0, 23, 10)
weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Foggy"])
road = st.selectbox("Road Type", ["Highway", "City", "Rural"])

# Encoding
weather_map = {"Clear": 0, "Rainy": 1, "Foggy": 2}
road_map = {"Highway": 0, "City": 1, "Rural": 2}

weather = weather_map[weather]
road = road_map[road]

if st.button("Predict Traffic Density"):
    X = np.array([[vehicles, time, weather, road]])
    prediction = model.predict(X)[0]
    st.success(f"🚘 Predicted Traffic Density: {prediction:.2f}")
