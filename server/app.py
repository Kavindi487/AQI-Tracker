from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/aqi_model.pkl")

def category(aqi):
    if aqi <= 50: return "Good"
    if aqi <= 100: return "Moderate"
    if aqi <= 150: return "Unhealthy (Sensitive)"
    if aqi <= 200: return "Unhealthy"
    if aqi <= 300: return "Very Unhealthy"
    return "Hazardous"

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    cat = None

    if request.method == "POST":
        X = pd.DataFrame([{
            "city": request.form["city"],
            "pm25": float(request.form["pm25"]),
            "co": float(request.form["co"]),
            "no2": float(request.form["no2"])
        }])

        prediction = round(float(model.predict(X)[0]), 1)
        cat = category(prediction)

    return render_template("index.html", prediction=prediction, category=cat)

if __name__ == "__main__":
    app.run(debug=True)
