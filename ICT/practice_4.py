# 1. Adulthood
age = int(input("Enter your age: "))
print("You are an adult" if age >= 18 else "You are a child")

# 2. Solve the following errors

# Code 1:
input1 = int(input('Enter a number:')) 
input2 = int(input('Enter another number:'))

# Code 2:
a = 6
if a == 6: 
    print('hello') 

# Code 3:
ask = bool(int(input('Do you want to make an calculation? (0/1)'))) 
if ask: 
    n = int(input('What is your number:'))
    print('Your number mulltiply by two is: ', n*2) 

# Code 4:
a = 0
if a == 0: print("It's a zero"), print('I think')

# 3. Calculator optimised
try:
    firstNumber = int(input("Enter a number: "))
    secondNumber = int(input("Enter a number: "))
    operation = input("Enter an operation (div/mul/add/sub): ")
    if (operation == "div"):
        print(firstNumber / secondNumber)
    elif (operation == "mul"):
        print(firstNumber * secondNumber)
    elif (operation == "add"):
        print(firstNumber + secondNumber)
    elif (operation == "sub"):
        print(firstNumber - secondNumber)
    else:    
        raise Exception("no such operation")
except ValueError:
    print("Sorry, the number you entered is not a number.")
except ZeroDivisionError:
    print("Sorry, a division by zero is impossible.")
except:
    print("error")