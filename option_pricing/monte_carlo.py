import numpy as np

class MonteCarloModel:
    def __init__(self, S0, X, T, r, sigma, q=0.0, num_simulations=10000, num_steps=252):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q
        self.num_simulations = num_simulations
        self.num_steps = num_steps

    def simulate_price_paths(self):
        dt = self.T / self.num_steps
        price_paths = np.zeros((self.num_simulations, self.num_steps + 1))
        price_paths[:, 0] = self.S0

        for t in range(1, self.num_steps + 1):
            z = np.random.standard_normal(self.num_simulations)
            price_paths[:, t] = price_paths[:, t-1] * np.exp(
                (self.r - self.q - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * z
            )

        return price_paths

    def option_price(self, option_type='call'):
        price_paths = self.simulate_price_paths()
        if option_type == 'call':
            payoffs = np.maximum(price_paths[:, -1] - self.X, 0)
        else:
            payoffs = np.maximum(self.X - price_paths[:, -1], 0)
        
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price
