v = []
while (True):
    a = int(input())
    if (a == 0):
        break
    v.append(a)
for i in range(len(v)):
    if (i > len(v) - i - 1): 
        break
    if (i == len(v) - i - 1): 
        print(v[i], end = ' ')
    else: 
        print(v[i] + v[(len(v) - i - 1)], end = ' ')
