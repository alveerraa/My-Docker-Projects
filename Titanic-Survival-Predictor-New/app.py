import streamlit as st
import pandas as pd
import pickle

# Load the trained model
import os

model_path = os.path.join(os.path.dirname(__file__), "titanic_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🚢 Titanic Survival Prediction")
st.write("Enter the passenger details to check if they would survive.")

# Input Fields
pclass = st.selectbox("Passenger Class (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
age = st.slider("Age", 1, 100, 30)
sibsp = st.slider("Number of Siblings/Spouses Aboard", 0, 8, 0)
parch = st.slider("Number of Parents/Children Aboard", 0, 6, 0)
fare = st.number_input("Fare ($)", 0, 500, 50)

# Prediction
if st.button("Predict Survival"):
    prediction = model.predict([[pclass, sex, age, sibsp, parch, fare]])
    result = "Survived! 🎉" if prediction[0] == 1 else "Did Not Survive 😢"
    st.subheader(result)

