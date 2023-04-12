dictionary = {}
while True:
    cmd = input('What do you want to do: add/delete/exit? ')
    if cmd == 'add':
        key = input('Enter the key: ')
        value = input('Enter the value: ')
        dictionary[key] = value
    elif cmd == 'delete':
        key = input('Enter the key: ')
        del dictionary[key]
    else:
        break

    print('here is dictionary')
    for key in dictionary.keys():
        print(f'\t- {key}: {dictionary[key]}')


