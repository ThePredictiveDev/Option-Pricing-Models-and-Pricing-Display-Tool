import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    def __init__(self, S0, X, T, r, sigma, q=0.0):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q

    def d1(self):
        return (np.log(self.S0 / self.X) + (self.r - self.q + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)

    def call_price(self):
        d1 = self.d1()
        d2 = self.d2()
        return self.S0 * np.exp(-self.q * self.T) * norm.cdf(d1) - self.X * np.exp(-self.r * self.T) * norm.cdf(d2)

    def put_price(self):
        d1 = self.d1()
        d2 = self.d2()
        return self.X * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S0 * np.exp(-self.q * self.T) * norm.cdf(-d1)
