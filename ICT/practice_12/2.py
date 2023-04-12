import random

choices = ['rock', 'paper', 'scissor']
choice = input('Choice (rock/paper/scissor): ')
move = choices[random.randrange(0, 3)]

print(f'Computer said "{move}" =>', end=' ')
if choice == 'rock' and move == 'paper':
    print('you lost')
elif choice == 'paper' and move == 'scissor':
    print('you lost')
elif choice == 'scissor' and move == 'rock':
    print('you lost')
elif choice == move:
    print('draw')
else:
    print('you won')
