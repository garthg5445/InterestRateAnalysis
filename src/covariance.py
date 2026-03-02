from pathlib import Path
import pandas as pd
from mean import getMean

#Find the coVariance between federal interest rates and inflation rates

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'

def getCovariance():
    total = 0.0
    count = 0
    df = pd.read_csv(data_path)

    #Get the y value means
    for values in df["Inflation Rate"]:
        if pd.notna(values):
            total += values
            count += 1
    inflation_mean = total / count
    rate_mean = getMean()

    ##Calculate the coVariance


    x_values = df["Effective Federal Funds Rate"]
    y_values = df["Inflation Rate"]

    cov_sum = 0.0
    cov_count = 0

    #zip allows iteration over both variables
    for x, y in zip(x_values, y_values):
        if pd.notna(x) and pd.notna(y):
            cov_sum += (x - rate_mean) * (y - inflation_mean)
            cov_count += 1

    covariance = cov_sum / (cov_count - 1)
    return covariance

if __name__ == "__main__":
    print("covariance : ", getCovariance())
