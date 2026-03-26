import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("data/aqi_data.csv")

X = df[["city", "pm25", "co", "no2"]]
y = df["aqi"]

preprocess = ColumnTransformer(
    transformers=[
        ("city", OneHotEncoder(handle_unknown="ignore"), ["city"])
    ],
    remainder="passthrough"
)

model = RandomForestRegressor(
    n_estimators=250,
    random_state=42
)

pipeline = Pipeline([
    ("preprocess", preprocess),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)
pred = pipeline.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred))
print("R2:", r2_score(y_test, pred))

os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/aqi_model.pkl")

print("Model trained and saved successfully")