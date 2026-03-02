import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'

df = pd.read_csv(data_path)

df["DATE"] = pd.to_datetime(df[["Year", "Month", "Day"]])

x = df["Effective Federal Funds Rate"]
y = df["Inflation Rate"]

#rates against inflation
plt.figure(figsize=(8,6))
plt.scatter(x, y, alpha=0.6, color='teal', label="Monthly data")

#line of best fit
mask = x.notna() & y.notna()
m, b = np.polyfit(x[mask], y[mask], 1)
plt.plot(x[mask], m * x[mask] + b, color='red', label="Best fit line")


plt.xlabel("Fed Interest Rate (%)")
plt.ylabel("Inflation Rate (%)")
plt.title("Covariance: Fed Interest Rate vs Inflation Rate")
plt.legend()
plt.show()

#Covariance Over Time

plt.figure(figsize=(10,5))

plt.plot(df["DATE"], df["Effective Federal Funds Rate"], label="Fed Interests Rate")
plt.plot(df["DATE"], df["Inflation Rate"], label="Inflation Rate")

plt.xlabel("Date")
plt.ylabel("Rate (%)")
plt.title("Fed Interest Rate vs Inflation Over Time")
plt.legend()
plt.show()
