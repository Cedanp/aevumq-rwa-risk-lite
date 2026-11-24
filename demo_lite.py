import numpy as np

def run_lite_monte_carlo(prices, sims=2000, horizon=30):
    arr = np.array(prices, dtype=float)
    rets = np.diff(arr) / arr[:-1]
    mu, sigma = float(np.mean(rets)), float(np.std(rets)) or 0.01
    z_score = (float(rets[-1]) - mu) / sigma
    trap_alert = z_score > 2.5

    paths = np.zeros((sims, horizon))
    paths[:, 0] = arr[-1]
    for t in range(1, horizon):
        shocks = np.random.normal(mu, sigma, sims)
        paths[:, t] = paths[:, t - 1] * (1.0 + shocks)

    prob_up = float(np.mean(paths[:, -1] > arr[-1]))
    kelly = round(min(0.25, max(0.0, (prob_up - (1.0 - prob_up) / 1.5) * 0.5)), 3)
    return {"prob_up": round(prob_up, 4), "half_kelly": kelly, "bubble_trap": trap_alert}

if __name__ == "__main__":
    sample = [2450.0, 2510.0, 2490.0, 2620.0, 2710.0, 2840.0]
    print("AevumQ Lite Simulation:", run_lite_monte_carlo(sample))
