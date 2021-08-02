class Counter:
    def __init__(self, start=0):
        self.count = start

Counter
x = Counter(10)
print(x.count)
x.count += 1
print(x.count)