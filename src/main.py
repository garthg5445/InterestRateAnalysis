import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from regimes import assign_regimes_sigma
from markov import transition_matrix, regime_statistics, markov_forecast
from mgf import mgf_by_regime
from chebyshev import chebyshev_violations

#Load data
project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data' / 'fed_interest_rates.csv'
df = pd.read_csv(data_path)
df["DATE"] = pd.to_datetime(df[["Year", "Month", "Day"]])

df = df.sort_values("DATE").reset_index(drop=True)

#Expectations and surprise shocks (Drop only null inflation rows)
#preprocessing
df = df.dropna(subset=["Inflation Rate"]).reset_index(drop=True)

#Compute expectations
df["expected"] = df["Inflation Rate"].rolling(window=5, min_periods=1).mean().shift(1)

# Compute surprise dataframe
df["surprise"] = df["Inflation Rate"] - df["expected"]

# Regimes
df["state"] = assign_regimes_sigma(df["surprise"], factor=0.8)


# Transition matrix for Markov chain
P = transition_matrix(df["state"])

#Regime stats
stats = regime_statistics(df["surprise"], df["state"])

#Markov forecast
df["markov_forecast"] = np.nan  #create new column in dataframe
for t in range(len(df) - 1):
    s = df.loc[t, "state"]   #current regime youre in
    df.loc[t + 1, "markov_forecast"] = markov_forecast(s, P, stats["mean"])

#MGF's
t_grid = np.linspace(-1, 1, 21)   #bounded between -1 and 1 with 21 intervals(inclusive)
mgfs = mgf_by_regime(df["surprise"], df["state"], t_grid)

#Chebyshev
df["cheb_violation"] = chebyshev_violations(df["surprise"], df["state"], stats, k=2)

#Output's
print("############################################")

print("Sample size: ",len(df))

print(df["state"].value_counts()) #How many observations were in each state

print("\nTransition Matrix:\n", P)

print("\nRegime Statistics:\n", stats) #shows the current stats for any of the 3 regimes at time = t

df_mgf = pd.DataFrame(mgfs)
df_mgf = df_mgf.sort_index()
print(df_mgf)
print("\nChebyshev Violation Rates:\n",
      df.groupby("state")["cheb_violation"].mean())

print("Sigma of surprises:", df["surprise"].std()) #average surprise size



# Step plot of regimes over time
plt.figure(figsize=(12,4))
plt.step(df['DATE'], df['state'], where='mid')
plt.xlabel('Date')
plt.ylabel('Regime State')
plt.title('Regimes over Time')
plt.show()

# Heatmap of transition matrix
sns.heatmap(P, annot=True, cmap='Blues', fmt=".2f")
plt.title('Markov Transition Matrix')
plt.show()

#chebychev .... Each regime has its own mean and standard deviation. Chebyshev violations tell you how
#often the actual surprise deviates more than k standard deviations from the mean of the current regime.(+- k=2sigma in this ex)
plt.figure(figsize=(12,4))
plt.scatter(df['DATE'], df['surprise'], c=df['cheb_violation'], cmap='coolwarm', label='Chebyshev violation')
plt.xlabel('Date')
plt.ylabel('Inflation Surprise')
plt.title('Chebyshev Violations Over Time')
plt.colorbar(label='Violation (True=1, False=0)')
plt.show()


#Regimes --> determined by shock magnitude and sign

#Markov chain --> models how shocks transition over time

#Chebyshev violations--> measure tail risk within each shock regime

#MGF's --> describe how fast tail risk decays inside each regime



