import pandas_datareader.data as web 
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2021,1,1)
end = dt.datetime(2021, 12, 25)

prices = web.DataReader('LTC', 'yahoo', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#Number of Simulations  #monte carlo
#variables
num_simulations = 500
num_days = 100

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
    
    simulation_df[x] = price_series
    
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: Litecoin ')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'g', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
