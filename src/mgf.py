import numpy as np

def computed_mgf(x, t):
    return np.mean(np.exp(t * x))

def mgf_by_regime(values, states, t_grid):
    mgfs = {}
    for state in states.unique():
        xs = values[states == state]
        mgfs[state] = {t: computed_mgf(xs, t) for t in t_grid}
    return mgfs
