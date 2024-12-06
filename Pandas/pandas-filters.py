import numpy as np
import pandas as pd

np_multi = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(np_multi, columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

result = df.columns
result = df.head()
result = df.head(10)
result = df.tail()
result = df['Column1'].head()
result = df.Column1.head()
result = df[['Column1', 'Column2']].head()
result = df[['Column1', 'Column2']][5:10]

result = df[df>50]
result = df[df['Column1']>50][['Column1', 'Column2']]
result = df[(df['Column1']>50) & (df['Column1']<70)]
result = df[(df['Column1']>50) | (df['Column1']<70)]
result = df.query('Column1 >= 50 & Column1 % 2 == 0')

# groupby
result = df.groupby('Column1').groups
# result = df.groupby('Column1').get_group('15')


print(result)