import streamlit as st
import pickle
import pandas as pd
import joblib

model = joblib.load('heart_model.pkl') 


# Load the model once when the app starts
#with open('heart_model.pkl', 'rb') as f: 
     #model = pickle.load(f)
#print("Model loaded successfully!")


st.title("Heart Disease Prediction")

# Create input fields for user data
age = st.number_input("Age", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (CP)", options=[0, 1, 2, 3], format_func=lambda x: f"Type {x}")
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1)
chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, step=1)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", options=[0, 1, 2, 3])
thal = st.selectbox("Thalassemia", options=[0, 1, 2, 3])



# Add other necessary input fields for your model

# If the user clicks the predict button
if st.button("Predict"):
    # Prepare the input data for prediction (convert it to DataFrame or numpy array)
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ]], columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"])  # Update with actual feature names

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    st.write(f'Prediction: {"Positive" if prediction[0] == 1 else "Negative"}')
