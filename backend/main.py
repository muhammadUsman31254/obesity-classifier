from fastapi import FastAPI
from typing import Optional, Annotated
from pydantic import BaseModel, Field
import pandas as pd
import pickle

# Load model
with open('obesity_ml_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Class mapping fallback
class_mapping = {
    1: "Underweight",
    2: "Normal",
    3: "Overweight",
    4: "Obesity"
}

# Define input schema
class ObesityFeatures(BaseModel):
    Sex: Annotated[int, Field(description="1: Male, 2: Female", example=2)]
    Age: Annotated[int, Field(description="Age in years", example=22)]
    Height: Annotated[int, Field(description="Height in cm", example=165)]
    Overweight_Obese_Family: Annotated[int, Field(description="1: Yes, 2: No", example=1)]
    Consumption_of_Fast_Food: Annotated[int, Field(description="1: Yes, 2: No", example=1)]
    Frequency_of_Consuming_Vegetables: Annotated[int, Field(description="1: Rarely, 2: Sometimes, 3: Always", example=2)]
    Number_of_Main_Meals_Daily: Annotated[int, Field(description="1: 1–2, 2: 3, 3: 3+", example=2)]
    Food_Intake_Between_Meals: Annotated[int, Field(description="1: Rarely, 2: Sometimes, 3: Usually, 4: Always", example=3)]
    Smoking: Annotated[int, Field(description="1: Yes, 2: No", example=2)]
    Liquid_Intake_Daily: Annotated[int, Field(description="1: <1L, 2: 1–2L, 3: >2L", example=2)]
    Calculation_of_Calorie_Intake: Annotated[int, Field(description="1: Yes, 2: No", example=2)]
    Physical_Excercise: Annotated[int, Field(description="1: None, 2: 1–2d, 3: 3–4d, 4: 5–6d, 5: 6+d", example=3)]
    Schedule_Dedicated_to_Technology: Annotated[int, Field(description="1: 0–2h, 2: 3–5h, 3: >5h", example=3)]
    Type_of_Transportation_Used: Annotated[int, Field(description="1: Automobile, 2: Motorbike, 3: Bike, 4: Public Transport, 5: Walking", example=4)]

# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Obesity Prediction API is running."}

@app.post("/predict")
def predict_obesity(data: ObesityFeatures):
    # Convert input to DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Predict class
    prediction = model.predict(df)[0]
    predicted_label = class_mapping.get(prediction, "Unknown")

    # Predict class probabilities
    probabilities = model.predict_proba(df)[0]
    confidence_score = float(round(max(probabilities), 4))  
    return {
        "predicted_class_numeric": int(prediction),
        "predicted_class_label": predicted_label,
        "confidence": confidence_score
    }
