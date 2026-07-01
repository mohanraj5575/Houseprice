import streamlit as st
import pickle
import numpy as np

# Load Trained Model
with open("model_pickle", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

# User Inputs
area = st.number_input("Area (sq.ft)", min_value=100, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)

# Prediction Button
if st.button("Predict House Price"):

    # Create input array
    input_data = np.array([[area, bedrooms, bathrooms]])

    # Predict
    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
