import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))  # IMPORTANT

st.set_page_config(page_title="Water Quality Predictor", layout="centered")

st.title("💧 Water Quality Prediction System")
st.markdown("Enter water parameters to check if it's safe to drink")

# Inputs
pH = st.number_input("pH (0-14)", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 1000.0, 200.0)
solids = st.number_input("Solids", 0.0, 100000.0, 15000.0)
chloramines = st.number_input("Chloramines", 0.0, 20.0, 7.0)
sulfate = st.number_input("Sulfate", 0.0, 1000.0, 300.0)
conductivity = st.number_input("Conductivity", 0.0, 2000.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 50.0, 10.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 200.0, 80.0)
turbidity = st.number_input("Turbidity", 0.0, 20.0, 4.0)

# Prediction
if st.button("Check Water Quality"):

    input_data = np.array([[pH, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])

    # Apply scaling (VERY IMPORTANT)
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    # Debug info
    st.write("Prediction value:", prediction[0])

    if prediction[0] == 1:
        st.success("✅ Water is SAFE to drink")
    else:
        st.error("❌ Water is NOT safe to drink")

# Footer
st.markdown("---")
st.caption("ML-Based Water Quality Prediction Project")