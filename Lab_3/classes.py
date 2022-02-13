from math import sqrt

class MyStrings:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string)

# x = MyStrings()
# x.getString()
# x.printString()

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__()
    
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.length * self.width

# x = Square(4)
# print(x.area())

# y = Rectangle(8, 2)
# print(y.area())

# z = Shape()
# print(z.area())

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, newX, newY):
        self.x = newX
        self.Y = newY

    def dist(self, x, y):
        print(sqrt((self.x - x)**2 + (self.y - y)**2))

# p = Point(0, 0)
# p.show()
# p.dist(3, 3)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance = self.balance + sum
    
    def withdraw(self, sum):
        if (self.balance < sum):
            print(f'Money on balance {self.balance}, can not withdraw {sum}')
        else:
            self.balance = self.balance - sum

# p = BankAccount('Alikhan', 999)
# p.deposit(1)
# p.withdraw(1001)
# p.withdraw(1000)
# p.deposit(99)
# p.withdraw(100)

def isPrime(x):
    if (x == 1):
        return False
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

numbers = []
for i in range(1, 101):
    numbers.append(i)
numbers = list(filter(lambda x: isPrime(x), numbers))
print(numbers)