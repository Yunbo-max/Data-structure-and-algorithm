import numpy as np
import pandas as pd

print(f'pi is {np.pi}')
print(f'pi is {34.43}')

tickers = ['AAPL','GOOG','IBM','FB','F','V', 'G', 'GE']
print(list(map(len,tickers)))

price_list = [('AAPL', 144.09), ('GOOGL', 911.71), ('MSFT', 69), ('FB', 150), ('WMT', 75.32)]
print(sorted(price_list, key = lambda x: x[1], reverse = True))
print(sorted(price_list, key = lambda x: x[0]))

price_list.sort(key = lambda x: x[1])
print(price_list)

class Stock:
    def __init__(self, ticker, open, close, volume):
        self.ticker = ticker
        self.open = open
        self.close = close
        self.volume = volume
        self.rate_return = float(close)/open - 1

    def update(self, open, close):
        self.open = open
        self.close = close
        self.rate_return = float(self.close)/self.open - 1

    def print_return(self):
        print(self.rate_return)

apple  = Stock('AAPL', 143.69, 144.09, 20109375)
google = Stock('GOOGL', 898.7, 911.7, 1561616)

print('\n')
apple.ticker
apple.print_return()
apple.update(912.8,913.4)
apple.print_return()
apple.ceo = 'Tim Cook'
print(dir(apple))

price_list = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
price_array = np.array(price_list)
print(price_array)

Ar = np.array([[1,3], [2,4]])
print(f'{Ar} {type(Ar)}')

print(Ar.shape)

print(Ar[0])
print(f'First column: {Ar[:,0]}')

np.log(price_array)
print(np.std(price_array))



price = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
s = pd.Series(price)
print(s)
s = pd.Series(price, index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(s)
s.index = [6,5,4,3,2,1]
print(s)
print(s[1:])
print(s[:-2])
print(s[4])
s[4] = 0
print(s)


s = pd.Series(price, name = 'Apple Prices')
print(s)
print(s.name)
print(s.describe())

time_index = pd.date_range('2017-01-01', periods = len(s), freq = 'D')
s.index = time_index
print(s)

s.index = [6,5,4,3,2,1]
print(s)
print(s[1])
print(s.loc[1])
print(s[2])
print(s.iloc[1])
print(s.iloc[0])

time_index = pd.date_range('2017-01-01', periods = len(s), freq = 'D')
s.index = time_index
print(s['2017-01-02':'2017-01-05'])
print('\n')
print(s[(s > np.mean(s)) & (s < np.mean(s) + 1.64*np.std(s))])


# dataframe
from datetime import datetime
dict = {'AAPL': [143.5,  144.09, 142.73, 144.18, 143.77],
        'GOOG': [898.7,  911.71, 906.69, 918.59, 926.99],
        'IBM':  [155.58, 153.67, 152.36, 152.94, 153.49]}
dates = pd.date_range('2017-07-03', periods = 5, freq = 'D')
df = pd.DataFrame(dict, index = dates)
print(df)
