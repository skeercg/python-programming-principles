f = open('test.txt', 'r')
first_number = int(f.readline())
second_number = int(f.readline())
third_number = int(f.readline())
f.close
f = open('test.txt', 'a')
f.write('\n' + str(first_number * second_number - third_number))
f.close()