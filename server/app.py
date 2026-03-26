from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)

CORS(
    app,
    resources={r"/api/*": {"origins": ["http://localhost:4200"]}},
    supports_credentials=False
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "aqi_model.pkl"
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
            return jsonify({"error": "Pollutant values must be non-negative"}), 400

        X = pd.DataFrame([{
            "city": city,
            "pm25": pm25,
            "co": co,
            "no2": no2
        }])

        predicted_aqi = round(float(model.predict(X)[0]), 1)

        return jsonify({
            "aqi": predicted_aqi,
            "category": category(predicted_aqi),
            "advice": advice(predicted_aqi),
            "inputs": {
                "city": city,
                "pm25": pm25,
                "co": co,
                "no2": no2
            }
        }), 200

    except ValueError:
        return jsonify({"error": "pm25, co, and no2 must be numeric values"}), 400
    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)