import ta.momentum
import pandas
import numpy

def std(arr):
    if len(arr) == 0:
        return 1e8
    
    summ = 0
    average = sum(arr)/len(arr)

    for i in range(len(arr)):
        summ += (arr[i] - average)**2

    std = pow(summ/len(arr), 0.5)

    return std

def get_average_rsi(close):
    average_rsi = []
    rsi = []

    for i in range(2, 12 + 1):
        rsi.append(ta.momentum.rsi(pandas.Series(close), i))

    for i in range(len(close)):
        avg = 0
        for j in range(len(rsi)):
            avg += rsi[j][i]/len(rsi)
        average_rsi.append(avg)

    return average_rsi

def get_position_size(returns_log, start_index):
    lookback = 24

    if start_index - lookback < 0: return 0

    inverse_volatility = std(returns_log[start_index - lookback: start_index + 1])

    position_size = 1/inverse_volatility/100

    return position_size

def get_drawdown_regime(cumulative_returns, mode):
    drawdowns = []
    max_return = -1
    for i in range(len(cumulative_returns)):
        max_return = max(max_return, cumulative_returns[i])
        drawdowns.append(max_return - cumulative_returns[i]) # drawdown has positive value

    lookback = 30
    direction = 0
    cutoff = 0.1
    if len(drawdowns) > lookback:
        if drawdowns[-1] > cutoff:
            if numpy.polyfit(y=drawdowns[len(drawdowns) - lookback: len(drawdowns)], x=range(1, lookback + 1), deg=1)[0] < 0:
                direction = -1
            else:
                direction = 1

    if drawdowns[-1] > cutoff:
        if mode == 0:
            return direction
        if mode == 1:
            return 0.5
    else:
        return 1


