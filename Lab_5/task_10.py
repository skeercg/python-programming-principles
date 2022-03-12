import re

file = open('row.txt', 'r')
text = file.read()
file.close()

print(re.sub('([a-z])([A-Z])', '\g<1>_\g<2>', text).lower())