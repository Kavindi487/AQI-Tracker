from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

model = joblib.load("model/aqi_model.pkl")

def category(aqi):
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

def advice_for(category_name):
    advice_map = {
        "Good": "Air quality is good. Safe for normal outdoor activities.",
        "Moderate": "Air quality is acceptable for most people.",
        "Unhealthy (Sensitive)": "Sensitive groups should reduce prolonged outdoor exertion.",
        "Unhealthy": "Everyone may begin to experience health effects.",
        "Very Unhealthy": "Health alert. Avoid outdoor activities if possible.",
        "Hazardous": "Serious health risk. Stay indoors and take precautions."
    }
    return advice_map.get(category_name, "No advice available.")

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "AQI Predictor backend is running"
    })

@app.post("/api/predict")
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        required_fields = ["city", "pm25", "co", "no2"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        city = str(data["city"]).strip()
        pm25 = float(data["pm25"])
        co = float(data["co"])
        no2 = float(data["no2"])

        if pm25 < 0 or co < 0 or no2 < 0:
            return jsonify({"error": "Pollutant values cannot be negative"}), 400

        X = pd.DataFrame([{
            "city": city,
            "pm25": pm25,
            "co": co,
            "no2": no2
        }])

        prediction = round(float(model.predict(X)[0]), 1)
        cat = category(prediction)

        return jsonify({
            "aqi": prediction,
            "category": cat,
            "advice": advice_for(cat),
            "inputs": {
                "city": city,
                "pm25": pm25,
                "co": co,
                "no2": no2
            }
        })

    except ValueError:
        return jsonify({"error": "pm25, co, and no2 must be valid numbers"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)