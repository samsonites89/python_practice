class MyCalc:
    def __init__(self):
        self.num = 1

    def multiply(self, x, y):
        return self.num * x * y

    @staticmethod
    def add(x, y):
        return x + y


print(MyCalc.add(1, 2))
c = MyCalc()
print(c.multiply(1, 2))
