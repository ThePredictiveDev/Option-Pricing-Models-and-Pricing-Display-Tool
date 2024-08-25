import numpy as np

class HestonModel:
    def __init__(self, S0, X, T, r, kappa, theta, sigma, v0, rho, num_simulations=10000, num_steps=252):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.v0 = v0
        self.rho = rho
        self.num_simulations = num_simulations
        self.num_steps = num_steps

    def simulate_price_paths(self):
        dt = self.T / self.num_steps
        S = np.zeros((self.num_simulations, self.num_steps + 1))
        v = np.zeros((self.num_simulations, self.num_steps + 1))

        S[:, 0] = self.S0
        v[:, 0] = self.v0

        for t in range(1, self.num_steps + 1):
            z1 = np.random.standard_normal(self.num_simulations)
            z2 = np.random.standard_normal(self.num_simulations)
            z2 = self.rho * z1 + np.sqrt(1 - self.rho ** 2) * z2

            v[:, t] = np.maximum(v[:, t-1] + self.kappa * (self.theta - v[:, t-1]) * dt +
                                 self.sigma * np.sqrt(v[:, t-1]) * np.sqrt(dt) * z1, 0)
            S[:, t] = S[:, t-1] * np.exp((self.r - 0.5 * v[:, t]) * dt + np.sqrt(v[:, t] * dt) * z2)

        return S

    def option_price(self, option_type='call'):
        price_paths = self.simulate_price_paths()
        if option_type == 'call':
            payoffs = np.maximum(price_paths[:, -1] - self.X, 0)
        else:
            payoffs = np.maximum(self.X - price_paths[:, -1], 0)
        
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price
