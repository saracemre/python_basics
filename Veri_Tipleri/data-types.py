"""
x = int(input("x: "))
y = int(input("y: ")) 

print(type(x))
print(type(y))

toplam = x + y
print(toplam)
"""

age = 18
weight = 58.5
name = "Emre"
isStudent = True

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))

# int to float
result = float(age)

print(result)
print(type(result))

# float to int
result = int(weight)

print(result)
print(type(result))

# bool to str
result = str(isStudent)

print(result)
print(type(result)) # "True"

# bool to int

result = int(isStudent)

print(result)
print(type(result))

# True == 1

result = bool(weight)

print(result)
print(type(result))