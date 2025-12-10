# Algorithmic Trading Backtesting Engine

A lightweight Python backtesting engine designed to explore trend-following signals, volatility-based position sizing, and drawdown-adjustment techniques applied to 1-minute OHLC data. The project focuses on understanding time-series behavior, experimenting with simple quantitative ideas, and organizing trading logic in a modular structure.

---

## Technical Structure

backtesting-engine/  
├── config/                 
│   ├── config.json         
│   └── config.py           
├── visuals/                
├── .gitignore              
├── BTC-1m.csv              
├── exchange.py             
├── main.py                 
├── performance.py          
├── risk.py                
├── signal.py               
└── README.md               


**Main**  
The entry point of the application. It orchestrates the backtesting pipeline by initializing the data loader, injecting configuration parameters, and executing the simulation loop that binds signals to the risk engine.

**Signal**  
Encapsulates the core trading logic. It handles the generation of raw directional signals (Long/Short/Neutral) based on trend-following algorithms (e.g., Fast/Slow Moving Average crossovers) independent of position sizing.

**Risk**  
Implements the risk management overlay. This module dynamically calculates position sizing.

**Performance**  
The analytics engine. It computes key performance metrics (Cumulative Return, Drawdown depths) and utilizes Matplotlib to render diagnostic visualizations, including equity curves and regime-change markers.

**Exchange**  
Handles data ingestion and order simulation. It simulates the execution of trade orders against historical price action under fees and slippage.

**Config**  
Separates code from configuration. Contains JSON-based parameters for strategy sensitivity (e.g., lookback periods, risk thresholds, ...), allowing for rapid experimentation without modifying the codebase.

---

## Performance Results for Naive Strategy  

### Signal Generation   

Signals are produced using two instant-trend moving averages with different speeds.  
A long or short signal is issued when the fast trend crosses the slow trend.

The signal visualization includes:
- price data  
- fast and slow trend lines  
- crossover signal markers  

This plot is used to verify whether the indicator and signal logic behave as intended.

![Price Timeseries](visuals/Timeseries.png)

### Risk Management  

**Volatility-Based Position Sizing**  
Position size is determined using a rolling volatility estimate derived from log returns.  
Higher volatility results in smaller exposures; lower volatility allows larger exposures.

**Drawdown-Based Exposure Adjustment**  
Cumulative returns are used to calculate drawdowns.  
When drawdowns exceed a defined threshold, the system shifts to a reduced-exposure regime.  
A polynomial fit is applied to recent drawdown values to estimate the slope of the drawdown period.

### Performance  
Two cumulative return curves are generated for comparison:

1. **Simple Strategy (volatility sizing only)**  
   Produces a relatively smooth upward curve due to consistent risk scaling.  
   Despite the smoother profile, the variability suggests modest risk-adjusted returns.

2. **Drawdown-Adjusted Strategy**  
   Exposure directly proportional to current drawdown.  
   In this configuration, the adjustment lowers overall performance and results in a more conservative equity curve, which was to be expected.

![Equity Curves](visuals/Strategies_Return.png)

These results (over a period of 7 years) illustrate how different exposure rules influence stability and overall performance, even when they reduce returns.

---

## Libraries and Tools

- Python  
- Pandas  
- NumPy  
- Ta
- Matplotlib  
- Json


- Standard time-series statistical methods

---

## Future Extensions

- Expand to multi-symbol backtesting  
- Introduce asynchronous or multiprocessing execution  




