# 1. Simple function
def greeting():
    name = input('Hello, give me your name: ')
    print('Hello', name, end='')
    print( ', welcome home. ')

# 2. Use arguments
def factorial():
    number = int(input())
    f = 1
    for i in range(1, number + 1):
        f *= i
    print(f)

# 3. Use optional arguments
def sum(end, start = 0, step = 1):
    sum = 0
    for i in range(start, end, step):
        sum += i
    return sum

# 4. The perfect number
def perfect_number(number):
    sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    return sum == number




