How It Works
The user opens the Angular frontend.
The user selects a city and enters pollutant values.
The frontend sends a POST request to the Flask backend.
The backend loads the trained ML model and predicts the AQI.
The predicted AQI, category, and health advice are returned as JSON.
The frontend displays the result with color-coded risk styling.
AQI Prediction Inputs

The system currently uses these features:

city
pm25
co
no2
AQI Categories

The predicted AQI is mapped into categories such as:

Good
Moderate
Unhealthy (Sensitive)
Unhealthy
Very Unhealthy
Hazardous
Backend API
Health Check

GET

/api/health

Sample response:

{
  "status": "ok",
  "message": "AQI Predictor backend is running"
}
Predict AQI

POST

/api/predict

Request body:

{
  "city": "Colombo",
  "pm25": 35,
  "co": 1.2,
  "no2": 40
}

Sample response:

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
Running the Project Locally
1. Clone the repository
git clone https://github.com/Kavindi487/AQI-Tracker.git
cd AQI-Tracker
Run the Backend

Go to the backend folder:

cd server

Install dependencies:

py -m pip install -r requirements.txt

Generate dataset:

py generate_data.py

Train model:

py train_model.py

Start Flask server:

py app.py

Backend will run on:

http://127.0.0.1:5000
Run the Frontend

Open a new terminal and go to:

cd aqi-client

Install dependencies:

npm install

Run Angular app:

ng serve

Frontend will run on:

http://localhost:4200
Example Test Values

Use these values in the dashboard for testing:

City: Colombo
PM2.5: 35
CO: 1.2
NO₂: 40
Machine Learning Overview

The backend model is trained using a pipeline that includes:

One-hot encoding for the city feature
Random Forest Regressor for AQI prediction

The current version uses synthetic AQI data generated for sample Sri Lankan cities.

Screens and Pages
Dashboard
Input pollutant values
Get AQI prediction
View category and advice
Cities
View a Sri Lanka city risk map
Explore low, medium, and high AQI risk zones
About
Learn about the project
View features and technology stack
Login / Register
UI pages prepared for future authentication support
Future Improvements
Use real environmental datasets
Add prediction history
Add AQI trend charts
Add user authentication with database support
Deploy frontend and backend
Add live air quality feeds
Author

Kavindi Vidusari
<img width="1919" height="965" alt="Screenshot 2026-03-26 103135" src="https://github.com/user-attachments/assets/71117dd2-b145-41b3-9527-4845299bf401" />
<img width="1908" height="964" alt="Screenshot 2026-03-26 103154" src="https://github.com/user-attachments/assets/bb9c9678-62f5-4524-ab96-d077d170c9d7" />
<img width="1919" height="978" alt="Screenshot 2026-03-26 103145" src="https://github.com/user-attachments/assets/71129e47-5e02-469b-aefc-2e5ecda9cdfb" />

License

This project is for learning and academic/project use
