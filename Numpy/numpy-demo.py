import numpy as np

result = np.array([10, 15, 30, 45, 60])
result = np.arange(5, 16)
result = np.arange(50, 100, 5)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0, 100, 5)
result = np.random.randint(10, 30, 5)
result = np.random.randn(10)

matrix = np.random.randint(10, 50, [3, 5])
rowTotal = matrix.sum(axis=1)
colTotal = matrix.sum(axis=0)
# print(rowTotal)
# print(colTotal)
print(matrix)
result = np.max(matrix)
result = np.min(matrix)
result = np.mean(matrix)
result = matrix.max()
result = matrix.argmax()

arr = np.arange(1, 10)
result = arr[:3]
result = arr[::-1]

result = matrix[0]
result = matrix[1, 2]
result = matrix[:, 0]
result = matrix**2

evens = matrix[matrix%2==0]
result = evens[evens>25]


print(result)