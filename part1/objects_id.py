
# get object id
x = [1, 2, 3]

print(id(x))
print(type(id(x)))
print(id([1, 2, 3]))


x = [4, 5, 6]
y = x
print(y is x)  # True
print(x is [4, 5, 6])  # False


x = [7, 8, 9]
y = x
print(y is x)
x.append(4)
print(x)
print(y)

print(id(x))
print(id(y))





