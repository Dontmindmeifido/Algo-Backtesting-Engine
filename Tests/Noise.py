from Main import close
import matplotlib.pyplot as plt
import ta
import ta.trend
import pandas
import ta.momentum

difference = [0]
for i in range(1, len(close)):
    difference.append(close[i] - close[i - 1])

def get_Noise(difference, lookback = 9):
    noise = []

    cur_sum = 0
    for i in range(len(difference)):
        cur_sum += abs(difference[i])
        if (i - lookback >= 0):
            cur_sum -= abs(difference[i - lookback])
        else:
            noise.append(0)
            continue
        
        bin_return = difference[i] - difference[i - lookback + 1]

        noise.append(bin_return/cur_sum)

    return noise

plt.subplot(3, 1, 1)
plt.plot(close)

plt.subplot(3, 1, 2)

noise = get_Noise(difference, 6000)
nm = []
for i in range(len(noise)):
    if i % 24 == 0:
        nm.append(noise[i])

plt.plot(noise)

plt.subplot(3, 1, 3)
plt.scatter(y=nm, x=range(len(nm)))

plt.show()




