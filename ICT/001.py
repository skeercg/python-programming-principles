# a = int(input())
# print('your number is between 0 and 10', (0 < a and a < 10))

a = int(input())
print((0 < a and a < 10) * 'Yes', end = ' ')
print((0 > a or a > 10) * 'No', end = ' ')
