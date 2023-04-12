# 1. 2. 3. 4.

jokeNotebook = {
    'Best joke ever': 'Why shouldn’t you eat clowns? They taste funny.'
}

while True:
    jokeName = input('Give a name to your joke: ')
    if jokeName == 'stop':
        break

    jokeContent = input('Tell me your joke: ')

    jokeNotebook[jokeName] = jokeContent

print('Here are the jokes:')
for key in jokeNotebook:
    print(f'Joke title: {key}. Joke: {jokeNotebook[key]}.')



# 5. Let the user choose 
myJokes = {
    'a': 'b',
    'c': 'd',
    'e': 'f',
    'x': 'y',
}

print('Here are all my jokes:')
for key in myJokes:
    print(f'- {key}')

chosenJoke = input('Which one do you want to see: ')
while chosenJoke not in myJokes:
    print('There is no such joke!')
    chosenJoke = input('Which one do you want to see: ')

print(f'Here is "{chosenJoke}": "{myJokes[chosenJoke]}."')