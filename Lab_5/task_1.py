import re

file = open('row.txt', 'r')
text = file.read()

print(re.findall('ab*', text))
