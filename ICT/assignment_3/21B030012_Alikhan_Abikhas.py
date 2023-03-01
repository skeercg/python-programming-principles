total = 0
while True:
    number = int(input('Enter a number between 1 and 10 (or 0 to exit):\n'))
    if 0 < number and number <= 10:
        total = total + number
        print('The sum of all your number is:', total)
    elif number == 0:
        print('The program is finished, the final sum is:', total)
        break
    else:
        print('Sorry, if the number is not between 0 and 10 it\'s too hard for me.')
