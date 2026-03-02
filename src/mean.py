from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'



def getMean():
    df = pd.read_csv(data_path)
    total = 0.0
    count = 0
    for value in df["Effective Federal Funds Rate"]:
        if pd.notna(value):
            total += value
            count += 1
    mean = total / count
    return mean

if __name__ == "__main__":
    print ("fed rate mean", getMean())


