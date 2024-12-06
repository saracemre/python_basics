import sqlite3
import pandas as pd

s1 = pd.Series([1, 2, 5, 3])
s2 = pd.Series([8, 3, 1, 0])

# data = {'apples': s1, 'oranges': s2}
data = dict(apples=s1, oranges=s2)
df = pd.DataFrame(data)

'''
 Reading Files

df = pd.read_csv('sample.csv')
df = pd.read_json('sample.json')
df = pd.read_excel('sample.xlsx')

connection = sqlite3.connect('sample.db')
df = pd.read_sql_query('SELECT * FROM students', connection)
'''



print(df)