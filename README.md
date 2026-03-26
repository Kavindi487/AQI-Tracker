# 🌿 AQI Tracker – Air Quality Prediction System

![Angular](https://img.shields.io/badge/Frontend-Angular-red?logo=angular)
![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![ML](https://img.shields.io/badge/Model-RandomForest-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

AQI Tracker is a full-stack web application that predicts Air Quality Index (AQI) values for Sri Lankan cities using machine learning.

It combines:
- 📊 Machine learning prediction
- 🌐 Flask REST API backend
- 💻 Angular frontend UI

---

## 🚀 Features

- Predict AQI using pollutant inputs  
- Real-time frontend → backend integration  
- Color-coded AQI risk visualization  
- Sri Lanka city risk map  
- Health advice based on AQI level  
- Clean and responsive UI  

---

## ⚙️ How It Works

1. The user opens the Angular frontend  
2. The user selects a city and enters pollutant values  
3. The frontend sends a POST request to the Flask backend  
4. The backend loads the trained ML model and predicts AQI  
5. The predicted AQI, category, and advice are returned as JSON  
6. The frontend displays results with color-coded styling  

---

## 📊 AQI Prediction Inputs

The system uses:

- city  
- pm25  
- co  
- no2  

---

## 🏷️ AQI Categories

- Good  
- Moderate  
- Unhealthy (Sensitive)  
- Unhealthy  
- Very Unhealthy  
- Hazardous  

---

## 🌐 Backend API

### 🔹 Health Check

GET  
/api/health  

Response:

```json
{
  "status": "ok",
  "message": "AQI Predictor backend is running"
}
```

---

### 🔹 Predict AQI

POST  
/api/predict  

Request:

```json
{
  "city": "Colombo",
  "pm25": 35,
  "co": 1.2,
  "no2": 40
}
```

Response:

```json
{
  "aqi": 95.4,
  "category": "Moderate",
  "advice": "Air quality is acceptable for most people.",
  "inputs": {
    "city": "Colombo",
    "pm25": 35,
    "co": 1.2,
    "no2": 40
  }
}
```

---

## ▶️ Running the Project Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Kavindi487/AQI-Tracker.git
cd AQI-Tracker
```

---

## 🖥️ Run Backend

```bash
cd server
py -m pip install -r requirements.txt
py generate_data.py
py train_model.py
py app.py
```

Backend runs at:  
http://127.0.0.1:5000  

---

## 💻 Run Frontend

```bash
cd aqi-client
npm install
ng serve
```

Frontend runs at:  
http://localhost:4200  

---

## 🧪 Example Test Values

- City: Colombo  
- PM2.5: 35  
- CO: 1.2  
- NO₂: 40  

---

## 🧠 Machine Learning Overview

- One-hot encoding for city  
- Random Forest Regressor  
- Synthetic dataset used for training  

Performance:
- MAE ≈ 7.4  
- R² ≈ 0.93  

---

## 🖥️ Screens and Pages

### 📊 Dashboard
- Input pollutant values  
- Get AQI prediction  
- View category and advice  

### 🗺️ Cities
- Sri Lanka map with risk levels  
- Low / Medium / High zones  

### ℹ️ About
- Project overview  
- Features and tech stack  

### 🔐 Login / Register
- UI ready for future authentication  

---

## 📸 Screenshots

![Dashboard](https://github.com/user-attachments/assets/71117dd2-b145-41b3-9527-4845299bf401)

![Cities Page](https://github.com/user-attachments/assets/bb9c9678-62f5-4524-ab96-d077d170c9d7)

![Login Page](https://github.com/user-attachments/assets/71129e47-5e02-469b-aefc-2e5ecda9cdfb)

---

## 🚀 Future Improvements

- Real-world dataset integration  
- AQI history tracking  
- Charts and analytics  
- Authentication system  
- Deployment (cloud)  
- Live AQI data feeds  

---

## 👩‍💻 Author

Kavindi Vidusari  

---

## 📜 License

This project is for academic and learning purposes.
