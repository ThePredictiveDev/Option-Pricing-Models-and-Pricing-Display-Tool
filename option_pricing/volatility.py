import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

class VolatilityMeasures:
    def __init__(self, price_series):
        self.price_series = price_series

    def historical_volatility(self, window=252):
        log_returns = np.log(self.price_series / self.price_series.shift(1)).dropna()
        if len(log_returns) < window:
            raise ValueError(f"Not enough data points for the specified window: {window}")
        return log_returns.rolling(window=window).std().iloc[-1] * np.sqrt(252)

    def implied_volatility(self, option_chain, S0, X, T, r, q=0.0, option_type='call'):
        def bs_price(sigma):
            d1 = (np.log(S0 / X) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
            d2 = d1 - sigma * np.sqrt(T)
            if option_type == 'call':
                return S0 * np.exp(-q * T) * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
            elif option_type == 'put':
                return X * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp(-q * T) * norm.cdf(-d1)
            else:
                raise ValueError("Invalid option type. Must be 'call' or 'put'.")

        # Ensure 'lastPrice' exists in the option_chain DataFrame
        if 'lastPrice' not in option_chain.columns:
            raise ValueError("The option_chain DataFrame must contain a 'lastPrice' column.")
        
        market_price = option_chain['lastPrice'].iloc[0]
        
        # Handle cases where the solver might fail
        try:
            implied_vol = brentq(lambda x: bs_price(x) - market_price, 1e-6, 5)
        except ValueError:
            implied_vol = np.nan
        
        return implied_vol
