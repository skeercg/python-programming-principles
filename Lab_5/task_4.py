import re

file = open('row.txt', 'r')
text = file.read()
file.close()

print(re.findall('[A-Z]{1}[a-z]+', text))
