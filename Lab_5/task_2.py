import re

file = open('row.txt', 'r')
text = file.read()
file.close()

print(re.findall('ab{2,3}', text))
