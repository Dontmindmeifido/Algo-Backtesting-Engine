import matplotlib.pyplot as plt
import pandas
from Strategy_Entry import get_signal
from Strategy_Risk import get_position_size
from Strategy_Risk import get_drawdown_regime
import math

# Initialize Market Data
asset_path = "BTC-1m.csv"
ohlc = pandas.read_csv(asset_path, usecols = [1, 2, 3, 4]).values.tolist()

close = [i[3] for i in ohlc]
open = [i[0] for i in ohlc]
return_log = [math.log(i[3]/i[0]) for i in ohlc]

# Initialize Entry
signal = get_signal([j[3]/2 + j[0]/2 for j in ohlc], 0.01, 0.001, plot=True)


# Direction, entry index
trade = [0, 0]
cumulative_return = [0]
cumulative_return_drawdown_adjusted_simple = [0]


if __name__ == "__main__":
    for i in range(len(close)):
        if signal[i] != 0:
            if trade[0] == 0:
                trade = [signal[i], i]
            else:
                percentage = math.log(close[trade[1]]/close[i])
                position_size = get_position_size(return_log, trade[1])
                drawdown_regime_simple = get_drawdown_regime(cumulative_return, 1)

                cumulative_return.append(cumulative_return[-1] - trade[0]*position_size*percentage)
                cumulative_return_drawdown_adjusted_simple.append(cumulative_return_drawdown_adjusted_simple[-1] - drawdown_regime_simple*trade[0]*position_size*percentage)

                trade = [signal[i], i]

    plt.xlabel("Trades")
    plt.ylabel("Strategy Log Return")

    plt.plot(cumulative_return, c="red", label="Cumulative Return")
    plt.plot(cumulative_return_drawdown_adjusted_simple, c="black", label="Cumulative Return (Drawdown Risk Adjustment)")
    plt.legend()
    plt.show()

