import numpy as np

class TrinomialTreeModel:
    def __init__(self, S0, X, T, r, sigma, N, option_type='call', q=0.0):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.sigma = sigma
        self.N = N
        self.option_type = option_type
        self.q = q

    def price(self):
        dt = self.T / self.N
        u = np.exp(self.sigma * np.sqrt(2 * dt))
        d = 1 / u
        m = 1
        q_u = ((np.exp((self.r - self.q) * dt / 2) - np.exp(-self.sigma * np.sqrt(dt / 2))) / 
               (np.exp(self.sigma * np.sqrt(dt / 2)) - np.exp(-self.sigma * np.sqrt(dt / 2)))) ** 2
        q_d = ((np.exp(self.sigma * np.sqrt(dt / 2)) - np.exp((self.r - self.q) * dt / 2)) / 
               (np.exp(self.sigma * np.sqrt(dt / 2)) - np.exp(-self.sigma * np.sqrt(dt / 2)))) ** 2
        q_m = 1 - q_u - q_d
        discount = np.exp(-self.r * dt)

        ST = np.zeros((2 * self.N + 1, ))
        ST[self.N] = self.S0

        for i in range(1, self.N + 1):
            ST[self.N + i] = ST[self.N + i - 1] * u
            ST[self.N - i] = ST[self.N - i + 1] * d

        option_values = np.zeros_like(ST)
        if self.option_type == 'call':
            option_values = np.maximum(0, ST - self.X)
        else:
            option_values = np.maximum(0, self.X - ST)

        for i in range(self.N - 1, -1, -1):
            for j in range(0, 2 * i + 1):
                option_values[j] = (q_u * option_values[j + 2] + 
                                    q_m * option_values[j + 1] + 
                                    q_d * option_values[j]) * discount

        return option_values[0]
