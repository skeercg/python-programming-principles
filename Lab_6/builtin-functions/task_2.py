s = input()
print(f'lowercase: {sum(map(str.islower, s))}')
print(f'uppercase: {sum(map(str.isupper, s))}')