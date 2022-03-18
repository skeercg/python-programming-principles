file = open('text.txt')

line_count = 0

for word in file:
    line_count = line_count + 1

print(line_count)