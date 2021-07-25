objects = [1, 2, 1, 2, 3]


a = set()

for obj in objects: # доступная переменная objects
    a.add(id(obj))

print(len(a))

