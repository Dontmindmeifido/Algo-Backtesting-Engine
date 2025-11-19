import matplotlib.pyplot as plt

def instant_trend(a, data):
    InstTrend = [data[0], data[1]]
    for i in range(2, len(data)):
        InstTrend.append( (a - (a/2)**2) * data[i] + (a*a/2)*data[i-1] - (a - 3*a*a/4)*data[i-2] + 2*(1 - a)*InstTrend[-1] - (1 - a)**2*InstTrend[-2])

    return InstTrend

def get_signal(close, fast = 0.2, slow = 0.18, plot = False):
    slow = instant_trend(slow, close)
    fast = instant_trend(fast, close)

    signal = [0]
    for i in range(1, len(close)):
        if (fast[i - 1] < slow[i - 1] and fast[i] > slow[i]):
            signal.append(1) # Bullish

            if plot:
                plt.scatter(i, close[i], color="green", marker="x")
        elif (fast[i - 1] > slow[i - 1] and fast[i] < slow[i]):
            signal.append(-1) # Bearish

            if plot:
                plt.scatter(i, close[i], color="red", marker="x")
        else:
            signal.append(0) # Neutral

    if plot:
        plt.plot(close)
        plt.plot(fast)
        plt.plot(slow)
        
        plt.show()

    return signal


