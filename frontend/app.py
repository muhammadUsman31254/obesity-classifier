import streamlit as st
import requests

st.set_page_config(page_title="Obesity Predictor", layout="centered")

st.title("🧘 Obesity Risk Classifier")
st.markdown("Fill out the form below to predict obesity risk class based on lifestyle data.")

# Form inputs
with st.form("obesity_form"):
    Sex = st.selectbox("Sex", [("Male", 1), ("Female", 2)])
    Age = st.number_input("Age (years)", min_value=5, max_value=100, value=22)
    Height = st.number_input("Height (cm)", min_value=100, max_value=250, value=165)
    Overweight_Obese_Family = st.selectbox("Family history of obesity", [("Yes", 1), ("No", 2)])
    Consumption_of_Fast_Food = st.selectbox("Consumes fast food?", [("Yes", 1), ("No", 2)])
    Frequency_of_Consuming_Vegetables = st.selectbox("Vegetable consumption", [
        ("Rarely", 1), ("Sometimes", 2), ("Always", 3)
    ])
    Number_of_Main_Meals_Daily = st.selectbox("Main meals per day", [
        ("1–2", 1), ("3", 2), ("3+", 3)
    ])
    Food_Intake_Between_Meals = st.selectbox("Snacking frequency", [
        ("Rarely", 1), ("Sometimes", 2), ("Usually", 3), ("Always", 4)
    ])
    Smoking = st.selectbox("Do you smoke?", [("Yes", 1), ("No", 2)])
    Liquid_Intake_Daily = st.selectbox("Daily water intake", [
        ("<1L", 1), ("1–2L", 2), (">2L", 3)
    ])
    Calculation_of_Calorie_Intake = st.selectbox("Counts calorie intake?", [("Yes", 1), ("No", 2)])
    Physical_Excercise = st.selectbox("Physical exercise per week", [
        ("None", 1), ("1–2 days", 2), ("3–4 days", 3), ("5–6 days", 4), ("6+ days", 5)
    ])
    Schedule_Dedicated_to_Technology = st.selectbox("Screen time per day", [
        ("0–2 hrs", 1), ("3–5 hrs", 2), (">5 hrs", 3)
    ])
    Type_of_Transportation_Used = st.selectbox("Transportation", [
        ("Automobile", 1), ("Motorbike", 2), ("Bike", 3), ("Public Transport", 4), ("Walking", 5)
    ])

    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare data
    input_data = {
        "Sex": Sex[1],
        "Age": Age,
        "Height": Height,
        "Overweight_Obese_Family": Overweight_Obese_Family[1],
        "Consumption_of_Fast_Food": Consumption_of_Fast_Food[1],
        "Frequency_of_Consuming_Vegetables": Frequency_of_Consuming_Vegetables[1],
        "Number_of_Main_Meals_Daily": Number_of_Main_Meals_Daily[1],
        "Food_Intake_Between_Meals": Food_Intake_Between_Meals[1],
        "Smoking": Smoking[1],
        "Liquid_Intake_Daily": Liquid_Intake_Daily[1],
        "Calculation_of_Calorie_Intake": Calculation_of_Calorie_Intake[1],
        "Physical_Excercise": Physical_Excercise[1],
        "Schedule_Dedicated_to_Technology": Schedule_Dedicated_to_Technology[1],
        "Type_of_Transportation_Used": Type_of_Transportation_Used[1]
    }

    # Call FastAPI backend
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        response.raise_for_status()
        result = response.json()

        st.success(f"🧾 Prediction: **{result['predicted_class_label']}** (Class {result['predicted_class_numeric']})")
    except Exception as e:
        st.error(f"❌ Error calling prediction API: {e}")
