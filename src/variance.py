from mean import getMean
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'
mean_rate = getMean()

def getVariance():    #variance = E[x^2] - (EX)^2
    df = pd.read_csv(data_path)

    total = 0.0
    count = 0

    for values in df["Effective Federal Funds Rate"]:
        if pd.notna(values):
            total += values ** 2
            count += 1
    expected_x_squared = total / count
    variance = expected_x_squared - (mean_rate ** 2)
    return variance

if __name__ == "__main__":
    print ("fed rate variance", getVariance())
