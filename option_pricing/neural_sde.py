import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

class NeuralSDEModel:
    def __init__(self, S0, X, T, r, neural_network, num_simulations=10000, num_steps=252):
        self.S0 = S0
        self.X = X
        self.T = T
        self.r = r
        self.neural_network = neural_network
        self.num_simulations = num_simulations
        self.num_steps = num_steps

    def simulate_price_paths(self):
        dt = self.T / self.num_steps
        S = np.zeros((self.num_simulations, self.num_steps + 1))
        S[:, 0] = self.S0

        for t in range(1, self.num_steps + 1):
            z = np.random.normal(size=self.num_simulations)
            drift_volatility = self.neural_network.predict(S[:, t-1].reshape(-1, 1))
        
            # Ensure that drift_volatility has the correct shape and unpack it correctly
            drift = drift_volatility[:, 0]
            volatility = drift_volatility[:, 1]
        
            S[:, t] = S[:, t-1] * np.exp((drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)

        return S



    def option_price(self, option_type='call'):
        price_paths = self.simulate_price_paths()
        if option_type == 'call':
            payoffs = np.maximum(price_paths[:, -1] - self.X, 0)
        else:
            payoffs = np.maximum(self.X - price_paths[:, -1], 0)
        
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price

def build_neural_network():
    model = models.Sequential()
    model.add(layers.Input(shape=(1,)))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(2, activation='linear'))  # Two outputs: drift and volatility
    model.compile(optimizer='adam', loss='mse')
    return model

def train_neural_network(price_data, neural_network, epochs=10, batch_size=32):
    X_train = price_data[:-1].reshape(-1, 1)
    y_train = np.diff(price_data).reshape(-1, 1)
    y_train = np.hstack([y_train, np.abs(y_train)])
    neural_network.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
