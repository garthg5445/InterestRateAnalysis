from pathlib import Path
import pandas as pd
from math import sqrt
from mean import getMean

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'

mean = getMean()

def getStandardDev():       ##sample standard deviation = sqrt[ sum(Xi - Xbar)^2 / n-1 ]
    df = pd.read_csv(data_path)
    total = 0.0
    count = 0
    for values in df["Effective Federal Funds Rate"]:
        if pd.notna(values):
            total += (values - mean) ** 2
            count += 1
    standard_deviation = sqrt( total / (count - 1) )
    return standard_deviation

if __name__ == "__main__":
    print ("fed rate standard deviation", getStandardDev())
