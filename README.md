# Option Pricing and Metrics Display Tool

## Overview

This project is a comprehensive tool designed to price options on popular indices and display all necessary metrics and tools for quantitative traders to make informed decisions. The project integrates multiple option pricing models, calculates the Greeks, and measures volatility, with real-time updates using live market data. The tool is implemented in Python and is designed to be used within Jupyter Notebooks, offering an intuitive and interactive user interface.

## Features

- **Multiple Option Pricing Models**:
  - Black-Scholes Model
  - Binomial Tree Model
  - Monte Carlo Simulation
  - Heston Model
  - Merton Jump Diffusion Model
  - Hull-White Model
  - Trinomial Tree Model

- **Real-Time Data Fetching**: 
  - The tool fetches live market data using Yahoo Finance and updates the option prices, Greeks, and volatility measures every minute.

- **Comprehensive Greeks Calculation**:
  - Delta, Gamma, Theta, Vega, Rho

- **Volatility Measures**:
  - Historical Volatility
  - Implied Volatility (placeholder for future implementation)

- **Interactive Visualizations**:
  - Price History
  - Volatility Comparison
  - Option Greeks Visualization

- **User Interface**:
  - Built using `ipywidgets` for an interactive and responsive experience within Jupyter Notebooks.

## Project Structure

```plaintext
option_pricing_project/
│
├── option_pricing/
│   ├── __init__.py
│   ├── data_fetching.py
│   ├── neural_sde.py
│   ├── black_scholes.py
│   ├── binomial_tree.py
│   ├── monte_carlo.py
│   ├── heston.py
│   ├── jump_diffusion.py
│   ├── hull_white.py
│   ├── trinomial.py
│   ├── greeks.py
│   ├── volatility.py
│   ├── visualizations.py
│
└── 01_option_pricing_tool.ipynb
```

### Key Modules

- **`data_fetching.py`**: Fetches live data from Yahoo Finance.
- **`neural_sde.py`**: Implements the Neural SDE option pricing model.
- **`black_scholes.py`**: Implements the Black-Scholes model for option pricing.
- **`binomial_tree.py`**: Implements the Binomial Tree model.
- **`monte_carlo.py`**: Implements the Monte Carlo Simulation for option pricing.
- **`heston.py`**: Implements the Heston model.
- **`jump_diffusion.py`**: Implements the Merton Jump Diffusion model.
- **`hull_white.py`**: Implements the Hull-White model.
- **`trinomial.py`**: Implements the Trinomial Tree model.
- **`greeks.py`**: Calculates the Greeks.
- **`volatility.py`**: Calculates historical and implied volatility.
- **`visualizations.py`**: Contains functions for generating visualizations.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Jupyter Notebook
- The following Python packages:
  - `numpy`
  - `scipy`
  - `pandas`
  - `yfinance`
  - `ipywidgets`
  - `matplotlib`
  - `tensorflow` (for Neural SDE)
  
You can install the required packages using the following command:

```bash
pip install numpy scipy pandas yfinance ipywidgets matplotlib tensorflow
```

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/ThePredictiveDev/option-pricing-project.git
   ```
2. Navigate to the project directory
3. Launch Jupyter notebook and main notebook

## Usage

1. **Start the Analysis**:
   - Open `01_option_pricing_tool.ipynb` in Jupyter Notebook.
   - Run the notebook cells to initialize the user interface.
   - Enter the required inputs such as the ticker symbol, strike price, and time to maturity.

2. **Select the Option Pricing Model**:
   - Use the dropdown menu to select the desired option pricing model (e.g., Black-Scholes, Binomial Tree, etc.).

3. **Choose the Visualization**:
   - Select the type of chart you want to view, such as Price History, Volatility Comparison, or Option Greeks.

4. **Start the Real-Time Analysis**:
   - Click the "Start Analysis" button. The tool will fetch live data, calculate the option price, Greeks, and volatility measures, and display the results.
   - The data and visualizations will update every minute with the latest market data.

5. **Interpret the Results**:
   - The option price, Greeks, and volatility measures are displayed in real-time.
   - The selected chart will visualize the data for easier interpretation.

6. **Stop the Analysis**:
   - To stop the real-time updates, simply stop the Jupyter Notebook cell execution.

## Features and Functionality

- **Real-Time Updates**:
  - The tool automatically fetches and processes live market data every minute, ensuring that the calculations are up-to-date.

- **Multiple Models**:
  - Supports a variety of option pricing models to suit different financial scenarios.

- **Comprehensive Metrics**:
  - Provides detailed calculations of the Greeks and volatility measures to help traders make informed decisions.

- **Interactive Visualizations**:
  - Displays dynamic charts that allow users to visualize price history, volatility, and option Greeks.


## Contributing

Contributions are welcome!

## License 

This project is licensed under the MIT License.



