import pandas as pd
#Regimes are "pockets" of probability density at a given time stamp, characterized by their own mean and standardDev.
#These regimes shift over time, causing us to change which characteristics best describe the given state
def compute_sigma(series):
    return series.std()

def assign_regime_sigma(x, sigma, factor=1.0):
    if x < -factor * sigma:
        return 0  # negative shock
    elif x > factor * sigma:
        return 2  # positive shock
    else:
        return 1  # neutral

def assign_regimes_sigma(series, factor=1.0):   #The series in this case is the shock values
    sigma = compute_sigma(series)
    if sigma == 0:
        # If surprises are constant, force a neutral regime
        return pd.Series([1] * len(series), index=series.index)
    return series.apply(assign_regime_sigma, sigma=sigma, factor=factor)
