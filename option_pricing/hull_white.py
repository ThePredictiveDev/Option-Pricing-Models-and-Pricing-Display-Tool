import numpy as np

class HullWhiteModel:
    def __init__(self, S0, X, T, r0, sigma, kappa, theta, v0, num_simulations=10000, num_steps=252):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r0 = r0
        self.sigma = sigma
        self.kappa = kappa
        self.theta = theta
        self.v0 = v0
        self.num_simulations = num_simulations
        self.num_steps = num_steps

    def simulate_price_paths(self):
        dt = self.T / self.num_steps
        S = np.zeros((self.num_simulations, self.num_steps + 1))
        r = np.zeros((self.num_simulations, self.num_steps + 1))

        S[:, 0] = self.S0
        r[:, 0] = self.r0

        for t in range(1, self.num_steps + 1):
            z1 = np.random.standard_normal(self.num_simulations)
            z2 = np.random.standard_normal(self.num_simulations)
            
            r[:, t] = r[:, t-1] + self.kappa * (self.theta - r[:, t-1]) * dt + self.v0 * np.sqrt(dt) * z1
            S[:, t] = S[:, t-1] * np.exp((r[:, t] - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * z2)

        return S

    def option_price(self, option_type='call'):
        price_paths = self.simulate_price_paths()
        if option_type == 'call':
            payoffs = np.maximum(price_paths[:, -1] - self.X, 0)
        else:
            payoffs = np.maximum(self.X - price_paths[:, -1], 0)
        
        option_price = np.exp(-self.r0 * self.T) * np.mean(payoffs)
        return option_price
