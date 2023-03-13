todos = []
while True:
    print('Here is the list: ')
    for i in todos:
        print('\t-', i)
    
    todo = input('What do you want to add: ')
    if todo == 'nothing':
        break

    todos.append(todo)

    
print('Here is the list: ')
for i in todos:
    print('\t-', i)

print('Goodbye')