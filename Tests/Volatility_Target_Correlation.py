from Strategy_Entry import get_Signal
from Main import close
from Main import returns
from Strategy_Risk import std
import matplotlib.pyplot as plt
import ta.trend
import pandas
import numpy

Signal = get_Signal(close)


# Direction, entry index
trade = [0, 0]
standalone_Return = [0, 0]
inverse_Volatility = [0, 0]
lookback = 14

for i in range(len(close)):
        if Signal[i] != 0:
            if trade[0] == 0:
                trade = [Signal[i], i]
            else:
                percentage = (close[trade[1]] - close[i])/close[trade[1]]

                if trade[1] - lookback + 1 >= 0:
                    standalone_Return.append(- trade[0]*percentage)
                    inverse_Volatility.append(1/std(returns[trade[1] - lookback + 1: trade[1] + 1]) - inverse_Volatility[-2])

                trade = [Signal[i], i]

''' Continous Volatility
lookback = 6
volatility = [0]
for i in range(len(close)):
    if i > lookback - 1:
        volatility.append(1/std(returns[i - lookback + 1: i + 1]))
    else:
        volatility.append(0)
'''

fig, ax1 = plt.subplots()
ax1.scatter(x=range(len(standalone_Return)), y=standalone_Return, s=0.1, color="blue")
ax1.plot(ta.trend.sma_indicator(pandas.Series(standalone_Return), 3), color="blue")
ax1.set_ylabel("Percent Returns", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.hlines(y=0, xmin=0, xmax=len(standalone_Return))
ax2 = ax1.twinx()
ax2.scatter(x=range(len(inverse_Volatility)), y=inverse_Volatility, color="red", s=0.1)
ax2.plot(ta.trend.sma_indicator(pandas.Series(inverse_Volatility), 1), color="red")
ax2.set_ylabel("Inverse Volatility (Position Sizing)", color="red")
ax2.tick_params(axis="y", labelcolor="red")
ax2.hlines(y=0, xmin=0, xmax=len(inverse_Volatility))

fig2, ax2 = plt.subplots()
lookback = 21
ms = []
for i in range(lookback - 1, len(inverse_Volatility)):
    m, b = numpy.polyfit(inverse_Volatility[i - lookback + 1: i + 1], standalone_Return[i - lookback + 1: i + 1], 1)
    ms.append(m)
ax2.plot(ms)

plt.show()

