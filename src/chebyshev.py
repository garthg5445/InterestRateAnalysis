

def chebyshev_violations(values, states, regime_stats, k=2):   #P(|X-mu| >= ksigma) <= 1/k^2
    violations = []  # A max of 25% will be violations

    for x, s in zip(values, states):
        mu = regime_stats.loc[s, "mean"]
        sigma = regime_stats.loc[s, "std"]
        violations.append(abs(x - mu) >= k * sigma)

    return violations
