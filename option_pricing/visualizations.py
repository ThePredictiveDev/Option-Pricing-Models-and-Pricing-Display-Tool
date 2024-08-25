import matplotlib.pyplot as plt
import numpy as np

class Visualizations:
    def __init__(self, data):
        self.data = data

    def plot_price_history(self, ticker):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Close'], label=f'{ticker} Closing Prices')
        plt.title(f'Historical Prices for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def plot_volatility(self, historical_vol, implied_vol):
        labels = ['Historical Volatility', 'Implied Volatility']
        values = [historical_vol, implied_vol]
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'orange'])
        plt.title('Volatility Comparison')
        plt.ylabel('Volatility')
        plt.show()

    def plot_greeks(self, delta, gamma, theta, vega, rho):
        labels = ['Delta', 'Gamma', 'Theta', 'Vega', 'Rho']
        values = [delta, gamma, theta, vega, rho]
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['green', 'red', 'purple', 'yellow', 'brown'])
        plt.title('Option Greeks')
        plt.ylabel('Value')
        plt.show()
