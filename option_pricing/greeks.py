import numpy as np
from scipy.stats import norm

class Greeks:
    def __init__(self, S0, X, T, r, sigma, q=0.0):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q  # Dividend yield

    def d1(self):
        return (np.log(self.S0 / self.X) + (self.r - self.q + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)

    def delta(self, option_type='call'):
        d1 = self.d1()
        if option_type == 'call':
            return np.exp(-self.q * self.T) * norm.cdf(d1)
        elif option_type == 'put':
            return np.exp(-self.q * self.T) * (norm.cdf(d1) - 1)

    def gamma(self):
        d1 = self.d1()
        return np.exp(-self.q * self.T) * norm.pdf(d1) / (self.S0 * self.sigma * np.sqrt(self.T))

    def theta(self, option_type='call'):
        d1 = self.d1()
        d2 = self.d2()
        first_term = - (self.S0 * norm.pdf(d1) * self.sigma * np.exp(-self.q * self.T)) / (2 * np.sqrt(self.T))
        
        if option_type == 'call':
            second_term = self.q * self.S0 * norm.cdf(d1) * np.exp(-self.q * self.T)
            third_term = self.r * self.X * np.exp(-self.r * self.T) * norm.cdf(d2)
            return (first_term - second_term - third_term) / 365  # Per-day theta
        elif option_type == 'put':
            second_term = self.q * self.S0 * norm.cdf(-d1) * np.exp(-self.q * self.T)
            third_term = self.r * self.X * np.exp(-self.r * self.T) * norm.cdf(-d2)
            return (first_term + second_term + third_term) / 365  # Per-day theta

    def vega(self):
        d1 = self.d1()
        return self.S0 * np.sqrt(self.T) * norm.pdf(d1) * np.exp(-self.q * self.T) / 100

    def rho(self, option_type='call'):
        d2 = self.d2()
        if option_type == 'call':
            return self.X * self.T * np.exp(-self.r * self.T) * norm.cdf(d2) / 100
        elif option_type == 'put':
            return -self.X * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2) / 100

    def all_greeks(self, option_type='call'):
        delta = self.delta(option_type)
        gamma = self.gamma()
        theta = self.theta(option_type)
        vega = self.vega()
        rho = self.rho(option_type)
        return delta, gamma, theta, vega, rho
