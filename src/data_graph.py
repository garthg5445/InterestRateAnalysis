import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from mean import getMean
from standard_deviation import getStandardDev


project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'

def graph_data():
    df = pd.read_csv(data_path)

    df["DATE"] = pd.to_datetime(df[["Year", "Month", "Day"]]) # need to convert the csv data into 1 date column
    rates = df["Effective Federal Funds Rate"]

    mean = getMean()
    std = getStandardDev()


    plt.figure(figsize=(10, 5))

    # Time series line
    plt.plot(df["DATE"], rates, label="Effective Federal Funds Rate")

    # Mean line
    plt.axhline(mean, linestyle="--", label="Mean")

    # ±1 standard deviation band
    plt.fill_between(
        df["DATE"],
        mean - std,
        mean + std,
        alpha=0.2,
        label="±1 Standard Deviation"
    )

    plt.xlabel("Year")
    plt.ylabel("Interest Rate (%)")
    plt.title("Federal Funds Rate with Mean and Standard Deviation Band")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    graph_data()
