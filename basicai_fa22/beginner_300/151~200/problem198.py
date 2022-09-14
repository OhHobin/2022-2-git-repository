ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
        
volatility = []
for i in range(1, len(ohlc)):
    volatility.append(ohlc[i][1]-ohlc[i][2])
print(volatility)