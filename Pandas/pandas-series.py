import pandas as pd

# data
numbers = [10, 20, 30, 40]
letters = ['a', 'b', 'c']
_dict = {'a':10, 'b':20, 'c':30, 'd':40}

pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series(5, [0, 1, 2, 3])
pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd'])
# pandas_series = pd.Series(_dict)
result = pandas_series[['a', 'b']]

print(result)
print(pandas_series)