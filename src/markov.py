import pandas as pd
import numpy as np

def transition_matrix(states):
    unique_states = sorted(states.unique())
    counts = pd.DataFrame(
        0,
        index=unique_states,
        columns=unique_states,
        dtype=float
    )

    for t in range(len(states) - 1):
        i = states.iloc[t]    #state at time t
        j = states.iloc[t + 1]  #state at time t+1
        counts.loc[i, j] += 1 #EX. if i = 1 and j = 2, then you have observed 1 count of 1-->2 and add a 1

    return counts.div(counts.sum(axis=1), axis=0)  #converts the total counts to probabilities

def regime_statistics(values, states):
    return (
        pd.DataFrame({"value": values, "state": states})
        .groupby("state")["value"]
        .agg(["mean", "std", "count"])
    )

def markov_forecast(current_state, transition_matrix, regime_means):
    return np.dot( transition_matrix.loc[current_state].values,regime_means.values ) #returns dot product between current state matrix and mean vector
