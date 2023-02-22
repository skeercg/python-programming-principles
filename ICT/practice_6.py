# 1. All numbers
d = 5
while d <= 50:
    print(d, end=' ')
    d = d + 1

# 2. The user division
number = int(input('Enter the number: '))

print(number)
while number % 2 == 0:
    print(number // 2, end=' ')
    number = number // 2

# 3. The crazy bot
text = input('Hello! ')
trial = 1
while text != 'Hello':
    if trial <= 3:
        text = input('I said hello, do you have something to say to me? ')
    elif trial <= 6:
        text = input('You have to say hello to me! ')
    else:
        text = input('I SAID HELLO, ANSWER HELLO! ') 
    trial = trial + 1
print('Thank you, how are you?')

# 4. The snail simple
depth = 30
days = 0
while depth > 0:
    days = days + 1
    depth = depth - 7
    if depth <= 0:
        break
    depth = depth + 5

print('The snail will exit in', days, 'days')

# 5. The snail complex
depth = int(input('Enter the depth of the well: '))
up = int(input('Enter the daily distance climbed by the snail: '))
down = int(input('Enter the night distance slide down by the snail: '))
days = 1
while depth > 0:
    days = days + 1
    depth = depth - up
    if depth <= 0:
        break
    depth = depth + down

print('The snail will exit in', days, 'days')

# 6. The snail complex with security 
depth = int(input('Enter the depth of the well: '))
up = int(input('Enter the daily distance climbed by the snail: '))
down = int(input('Enter the night distance slide down by the snail: '))
while up <= down:
    print('No sorry, the daily distance has to be bigger than the night distance, enter them again! ')
    up = int(input('Enter the daily distance climbed by the snail: '))
    down = int(input('Enter the night distance slide down by the snail: '))
days = 0
while depth > 0:
    days = days + 1
    depth = depth - up
    if depth <= 0:
        break
    depth = depth + down

print('The snail will exit in', days, 'days')

