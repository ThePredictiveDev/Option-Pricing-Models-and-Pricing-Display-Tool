import numpy as np

class BinomialTreeModel:
    def __init__(self, S0, X, T, r, sigma, N):
        self.S0 = S0  # Initial stock price
        self.X = X  # Strike price
        self.T = T  # Time to maturity
        self.r = r  # Risk-free rate
        self.sigma = sigma  # Volatility
        self.N = N  # Number of time steps

        # Ensure parameters are realistic
        if T <= 0:
            raise ValueError("Time to maturity T must be positive")
        if sigma <= 0:
            raise ValueError("Volatility sigma must be positive")
        if r < 0:
            raise ValueError("Risk-free rate r must be non-negative")

        # Calculate derived parameters
        self.dt = T / N
        self.u = np.exp(sigma * np.sqrt(self.dt))
        self.d = 1 / self.u
        self.p = (np.exp(r * self.dt) - self.d) / (self.u - self.d)

        # Validate up/down factors and probability
        if not (0 < self.d < 1 < self.u):
            raise ValueError("The up/down factors are not correctly calculated")
        if not (0 < self.p < 1):
            raise ValueError("The probability is not in the valid range")

    def price(self, option_type='call'):
        # Initialize asset prices at maturity
        ST = np.zeros(self.N + 1)
        for i in range(self.N + 1):
            ST[i] = self.S0 * (self.u ** i) * (self.d ** (self.N - i))
        
        # Initialize option values at maturity
        if option_type == 'call':
            option_values = np.maximum(ST - self.X, 0)
        elif option_type == 'put':
            option_values = np.maximum(self.X - ST, 0)

        # Step backwards through tree
        for j in range(self.N - 1, -1, -1):
            for i in range(j + 1):
                option_values[i] = np.exp(-self.r * self.dt) * (self.p * option_values[i + 1] + (1 - self.p) * option_values[i])

        return option_values[0]
