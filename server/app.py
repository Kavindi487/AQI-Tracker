from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)

# Allow Angular frontend
CORS(
    app,
    resources={r"/api/*": {"origins": ["http://localhost:4200"]}},
    supports_credentials=False
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "aqi_model.pkl"

# Load trained ML pipeline
model = joblib.load(MODEL_PATH)


def category(aqi: float) -> str:
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Moderate"
    if aqi <= 150:
        return "Unhealthy (Sensitive)"
    if aqi <= 200:
        return "Unhealthy"
    if aqi <= 300:
        return "Very Unhealthy"
    return "Hazardous"


def advice(aqi: float) -> str:
    if aqi <= 50:
        return "Air quality is satisfactory and poses little or no risk."
    if aqi <= 100:
        return "Air quality is acceptable for most people."
    if aqi <= 150:
        return "Sensitive groups should reduce prolonged outdoor exertion."
    if aqi <= 200:
        return "Reduce outdoor activity and avoid heavy exertion."
    if aqi <= 300:
        return "Avoid outdoor activity if possible and stay protected."
    return "Stay indoors as much as possible and use protection outdoors."


@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "AQI Predictor backend is running"
    }), 200


@app.post("/api/predict")
def predict():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        required_fields = ["city", "pm25", "co", "no2"]
        missing = [field for field in required_fields if field not in data]

        if missing:
            return jsonify({
                "error": "Missing required fields",
                "missing": missing
            }), 400

        city = str(data["city"]).strip()
        pm25 = float(data["pm25"])
        co = float(data["co"])
        no2 = float(data["no2"])

        if pm25 < 0 or co < 0 or no2 < 0:
            return jsonify({
                "error": "Pollutant values must be non-negative"
            }), 400

        X = pd.DataFrame([{
            "city": city,
            "pm25": pm25,
            "co": co,
            "no2": no2
        }])

        predicted_aqi = round(float(model.predict(X)[0]), 1)
        aqi_category = category(predicted_aqi)

        return jsonify({
            "aqi": predicted_aqi,
            "category": aqi_category,
            "advice": advice(predicted_aqi),
            "inputs": {
                "city": city,
                "pm25": pm25,
                "co": co,
                "no2": no2
            }
        }), 200

    except ValueError:
        return jsonify({
            "error": "pm25, co, and no2 must be numeric values"
        }), 400
    except Exception as e:
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500


# Optional placeholder endpoints for your current login/register UI
@app.post("/api/register")
def register():
    try:
        data = request.get_json()

        full_name = str(data.get("fullName", "")).strip()
        email = str(data.get("email", "")).strip()
        password = str(data.get("password", "")).strip()
        confirm_password = str(data.get("confirmPassword", "")).strip()

        if not full_name or not email or not password or not confirm_password:
            return jsonify({"error": "All fields are required"}), 400

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match"}), 400

        return jsonify({
            "message": "Registration successful (demo backend)",
            "user": {
                "fullName": full_name,
                "email": email
            }
        }), 201

    except Exception as e:
        return jsonify({
            "error": "Registration failed",
            "details": str(e)
        }), 500


@app.post("/api/login")
def login():
    try:
        data = request.get_json()

        email = str(data.get("email", "")).strip()
        password = str(data.get("password", "")).strip()

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        return jsonify({
            "message": "Login successful (demo backend)",
            "token": "demo-token-12345",
            "user": {
                "email": email
            }
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Login failed",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)