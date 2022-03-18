file = open('write.txt', 'w')

values = ['alikhan', 'batyrbek', 'sakzhan']

for element in values:
    file.write(f'{element} ')