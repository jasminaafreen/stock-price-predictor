import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("📊 Stock Price Predictor")

prev_price = st.number_input("Enter Previous Day Closing Price")

if st.button("Predict"):
    prediction = model.predict([[prev_price]])
    st.success(f"Predicted Price: {prediction[0]:.2f}")
