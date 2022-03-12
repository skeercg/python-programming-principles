import re

file = open('row.txt', 'r')
text = file.read()
file.close()

print(re.sub('(\w)([A-Z])', '\g<1> \g<2>', text))