numbers = [0, 1, 2, 0, 0, 1, 2, 2, 1, 0, 1, 2]

choices = ['rock', 'scissors', 'paper']

comp_score = 0
player_score = 0

print('Welcome to the game')
for i in numbers:
    choice = input('Enter your choice (rock/scissors/paper): ')
    if choice == 'stop':
        break
    while choice not in choices:
        choice = input('Enter your choice (rock/scissors/paper): ')
    if choice == choices[i]:
        print('Egality!', end=' ')
    elif choice == 'paper' and choices[i] == 'rock':
        print('You won!', end=' ')
        player_score += 1
    elif choice == 'paper' and choices[i] == 'scissors':
        print('You lost!', end=' ')
        comp_score += 1
    elif choice == 'rock' and choices[i] == 'paper':
        print('You lost!', end=' ') 
        comp_score += 1
    elif choice == 'rock' and choices[i] == 'scissors':
        print('You won!', end=' ')
        player_score += 1
    elif choice == 'scissors' and choices[i] == 'rock':
        print('You lost!')
        comp_score += 1
    elif choice == 'scissors' and choices[i] == 'paper':
        print('You won!', end=' ')
        player_score += 1
    print('(You: ' + str(player_score) + ', Computer: ' + str(comp_score) + ')')

print('End of the game, the winner is ' + 'You' if player_score > comp_score else 'Computer')