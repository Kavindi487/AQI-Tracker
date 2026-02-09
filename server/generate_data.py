import pandas as pd
import numpy as np

np.random.seed(42)

cities = ["Colombo", "Kandy", "Galle"]
rows = []

for _ in range(2500):
    city = np.random.choice(cities)

    pm25 = np.random.uniform(5, 180)
    co = np.random.uniform(0.1, 4.0)
    no2 = np.random.uniform(5, 150)

    city_bias = {"Colombo": 15, "Kandy": 8, "Galle": 5}[city]
    aqi = (pm25 * 0.6) + (co * 12) + (no2 * 0.25) + city_bias + np.random.normal(0, 8)

    aqi = float(np.clip(aqi, 0, 500))
    rows.append([city, round(pm25, 2), round(co, 2), round(no2, 2), round(aqi, 1)])

df = pd.DataFrame(rows, columns=["city", "pm25", "co", "no2", "aqi"])
df.to_csv("data/aqi_data.csv", index=False)

print(" AQI dataset created")
