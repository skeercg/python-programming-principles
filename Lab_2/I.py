n = int(input())
a = []
for i in range(n):
    x = input().split()
    if (len(x) == 2): 
        a.append(x[1])
    else: 
        print(a[0], end = ' ')
        a.pop(0)