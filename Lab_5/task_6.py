import re

file = open('row.txt', 'r')
text = file.read()
file.close()

print(re.sub('\.| |,', ':', text))
