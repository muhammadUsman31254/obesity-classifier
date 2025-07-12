# 🧠 Obesity Risk Classifier — ML App (FastAPI + Streamlit)

This project is a full-stack machine learning web application that predicts obesity risk class based on lifestyle and dietary patterns. It includes:

- ⚙️ **FastAPI backend** to serve the trained ML model
- 🎨 **Streamlit frontend** for interactive UI
- 📦 **Random Forest Classifier** trained on real obesity dataset from [Kaggle](https://www.kaggle.com/datasets/suleymansulak/obesity-dataset)

---

## 📁 Project Structure

```
obesity-app/
├── backend/
│   ├── main.py                    # FastAPI app with prediction endpoint
│   ├── obesity_ml_model.pkl       # Trained model
│   └── requirements.txt           # Dependencies for FastAPI
├── frontend/
│   ├── streamlit_app.py           # Streamlit UI
│   └── requirements.txt           # Dependencies for Streamlit
└── README.md                      
```

---

## 🚀 How to Run Locally

### 🔹 1. Start FastAPI Backend

```bash
cd obesity-app/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at: `http://127.0.0.1:8000`

Test endpoint: `http://127.0.0.1:8000/docs`

### 🔹 2. Start Streamlit Frontend

Make sure the backend is running, then:

```bash
cd ../frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

UI will open in your browser: `http://localhost:8501`

---

## 🧠 Model

The model is trained on:

* **Features**: lifestyle, food habits, physical activity
* **Labels**: Underweight, Normal, Overweight, Obesity
* **Algorithm**: Random Forest Classifier

---

## 📊 Dataset Features

The model uses the following input features:

- **Demographics**: Age, Gender, Height, Weight
- **Eating Habits**: Frequency of high caloric food consumption, vegetable consumption, main meals per day
- **Physical Activity**: Physical activity frequency, time using technology devices
- **Lifestyle**: Water consumption, alcohol consumption, smoking habits, transportation mode
- **Medical**: Family history of overweight, monitoring calorie consumption

---

## 🔧 API Endpoints

### POST `/predict`

Predicts obesity risk class based on input features.

**Request Body:**
```json
{
  "age": 25,
  "gender": "Male",
  "height": 1.75,
  "weight": 70,
  "family_history_overweight": "yes",
  "frequent_high_caloric_food": "no",
  "vegetable_consumption": "sometimes",
  "main_meals": 3,
  "food_between_meals": "sometimes",
  "smoke": "no",
  "water_consumption": 2.5,
  "calorie_monitoring": "no",
  "physical_activity": "sometimes",
  "technology_use": 2,
  "alcohol_consumption": "no",
  "transportation": "public_transport"
}
```

**Response:**
```json
{
  "prediction": "Normal_Weight",
  "confidence": 0.85
}
```

---

## 🛠️ Dependencies

### Backend (FastAPI)
```
fastapi
uvicorn
pydantic
pandas
scikit-learn
```

### Frontend (Streamlit)
```
streamlit
requests
pandas
```

## 🙏 Acknowledgments

- Dataset from [Kaggle - Obesity Dataset](https://www.kaggle.com/datasets/suleymansulak/obesity-dataset)
- Built with [FastAPI](https://fastapi.tiangolo.com/) and [Streamlit](https://streamlit.io/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)

---

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**⭐ Star this repository if you found it helpful!**