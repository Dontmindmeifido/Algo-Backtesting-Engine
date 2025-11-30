# Algorithmic Trading Backtesting Engine

A lightweight Python backtesting engine designed to explore trend-following signals, volatility-based position sizing, and drawdown-adjustment techniques applied to 1-minute OHLC data. The project focuses on understanding time-series behavior, experimenting with simple quantitative ideas, and organizing trading logic in a modular structure.

---

## Overview

The system processes 1-minute market data, generates trading signals using custom “instant trend” moving averages, applies risk-based position sizing, and visualizes performance through cumulative return plots. The codebase is divided into separate modules to maintain clarity between signal logic, risk logic, and the backtest loop.

---

## Signal Generation

Signals are produced using two instant-trend moving averages with different speeds.  
A long or short signal is issued when the fast trend crosses the slow trend.

The signal visualization includes:
- price data  
- fast and slow trend lines  
- crossover signal markers  

This plot is used to verify whether the indicator and signal logic behave as intended.

![Price Timeseries](Visuals/Timeseries.png)

---

## Risk Management

### Volatility-Based Position Sizing  
Position size is determined using a rolling volatility estimate derived from log returns.  
Higher volatility results in smaller exposures; lower volatility allows larger exposures.

### Drawdown-Based Exposure Adjustment  
Cumulative returns are used to calculate drawdowns.  
When drawdowns exceed a defined threshold, the system shifts to a reduced-exposure regime.  
A polynomial fit is applied to recent drawdown values to estimate the slope of the drawdown period.

---

## Performance Results

Two cumulative return curves are generated for comparison:

1. **Simple Strategy (volatility sizing only)**  
   Produces a relatively smooth upward curve due to consistent risk scaling.  
   Despite the smoother profile, the variability suggests modest risk-adjusted returns.

2. **Drawdown-Adjusted Strategy**  
   Reduces exposure during deeper drawdown periods.  
   In this configuration, the adjustment lowers overall performance and results in a more conservative equity curve.

![Equity Curves](Visuals/Strategies_Return.png)

These results illustrate how different exposure rules influence stability and overall performance, even when they reduce returns.

---

## Tools and Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- ta.momentum (RSI calculations)  
- numpy.polyfit  
- Standard time-series statistical methods

---

## Future Extensions

- Add transaction costs and slippage  
- Compute performance metrics (Sharpe, CAGR, maximum drawdown)  
- Expand to multi-symbol backtesting  
- Introduce asynchronous or multiprocessing execution  
- Add configuration files for parameter management  
- Improve modularity and testing coverage




