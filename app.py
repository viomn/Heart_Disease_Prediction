import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("heart_disease.pkl", "rb"))

# App title and description
st.title("Heart Disease Prediction App")
st.write("""
This app predicts the likelihood of heart disease based on your health parameters.
Fill in the details below and click 'Predict' to see the result.
""")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1, help="Enter your age.")
sex = st.selectbox("Sex", options=["Male", "Female"], help="Select your biological sex.")
cp = st.selectbox("Chest Pain Type", options=[
    "Typical Angina",
    "Atypical Angina",
    "Non-anginal Pain",
    "Asymptomatic"
], help="Type of chest pain experienced.")
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=120, step=1, help="Enter your resting blood pressure.")
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200, step=1, help="Enter your serum cholesterol level.")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"], help="Indicate if fasting blood sugar exceeds 120 mg/dl.")
restecg = st.selectbox("Resting Electrocardiographic Results", options=[
    "Normal",
    "Having ST-T wave abnormality",
    "Showing probable/definite left ventricular hypertrophy"
], help="Select your resting ECG results.")
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150, step=1, help="Enter the maximum heart rate achieved.")
exang = st.selectbox("Exercise Induced Angina", options=["Yes", "No"], help="Select if exercise causes angina.")
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1, help="Enter the value of ST depression.")
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"], help="Select the slope of the ST segment.")
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, value=0, step=1, help="Enter the number of major vessels (0-3).")
thal = st.selectbox("Thalassemia", options=[
    "Normal",
    "Fixed Defect",
    "Reversible Defect"
], help="Select the type of thalassemia.")

# Map categorical inputs to numerical values for the model
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0
cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
restecg = ["Normal", "Having ST-T wave abnormality", "Showing probable/definite left ventricular hypertrophy"].index(restecg)
slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

# Prediction button
if st.button("Predict"):
    # Prepare input for the model
    features = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    prediction = model.predict(features)[0]

    # Display the result
    if prediction == 1:
        st.error("The model predicts you are at risk of heart disease. Please consult a doctor.")
    else:
        st.success("The model predicts you are NOT at risk of heart disease. Stay healthy!")

# Footer
st.write("Developed by Yazdan Haider Khan and Neha, using Streamlit and Machine Learning.")
