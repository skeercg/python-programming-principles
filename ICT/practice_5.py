# 1. All numbers

for i in range(5, 51, 1):
    print(i, end = ' ')

# 2. Give user information

st = int(input("Enter the start "))
en = int(input("Enter the end "))
step = int(input("Enter the step "))

for i in range(st, en, step):
    print(i, end = '-')

# 3. The pyramid

height = int(input("Enter the height of the pyramid "))

max_width = height * 2 - 1
for i in range(height):
    width = i * 2 + 1
    empty_space = (max_width - width) // 2
    print((empty_space * ' ') + (width * '*') + (empty_space * ' '))


# 4. The complex pyramid

max_width = int(input("Enter the width of the pyramid "))

height = (max_width + 1) // 2

for i in range(height):
    width = i * 2 + 1
    empty_space = (max_width - width) // 2
    print((empty_space * ' ') + (width * '*') + (empty_space * ' '))

# 5. Prime numbers

number = int(input("Enter a number: "))
for d in range(2, number, 1):
    if (number % d == 0):
        print("No because:", number // d, 'x', d, '=', number)
        break
else:
    print("It’s a prime number.")