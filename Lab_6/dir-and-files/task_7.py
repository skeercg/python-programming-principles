file1 = open('read_from.txt', 'r')
file2 = open('write_to.txt', 'w')

for i in file1:
    file2.write(i)