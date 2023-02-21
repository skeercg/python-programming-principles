#1. Adulthood
age = int(input('Enter your age: '))

if age > 18:
    print('You are an adult')
else:
    print('You are a child')

#2. Checking the user input
number = input('Enter a number (0 or 1): ')

if number == '0' or number == '1':
    print('Thanks!')
else:
    print('I said 0 or 1!')

#3. Multiples
number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))

if number1 % number2 == 0: 
    print('Yes,', number1, 'is a multiple of', number2, 'because', number2, 'x', number1 // number2, '=', number1)
else:
    print('No', number1, 'is not a multiple of', number2, '.')

#4. Leap year
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('This is a leap year.')
else: 
    print('This is a not a leap year.')

