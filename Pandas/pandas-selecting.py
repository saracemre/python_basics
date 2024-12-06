import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index=['a', 'b', 'c'], columns=['Column1', 'Column2', 'Column3'])

result = df['Column1']
result = df[['Column1', 'Column2']]

# loc['row', 'column']
result = df.loc['a']
result = df.loc[:, "Column1"]
result = df.loc[:, "Column1":"Column3"]
result = df.iloc[0]
result = df.loc[['a', 'c'], ['Column1', 'Column2']]

df['Column4'] = pd.Series(randn(3), ['a', 'b', 'c'])
df.drop("Column4", axis=1, inplace=True)

print(df)