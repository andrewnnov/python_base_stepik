class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if self.capacity - self.count - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.count += v


x = MoneyBox(10)

x.add(3)
print(x.count)
x.add(2)
print(x.count)
x.add(4)
print(x.count)
x.add(1)
print(x.count)
x.add(1)
print(x.count)