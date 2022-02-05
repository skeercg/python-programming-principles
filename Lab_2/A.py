from math import fabs


a = list(map(int, input().split()))
f = []
for i in range(len(a)):
    f.append(False)
f[0] = True
for i in range(len(a)):
    if (f[i] == True):
        for j in range(a[i] + 1):
            if (i + j < len(a)): 
                f[i + j] = True

if (f[len(a) - 1]): print(1)
else: print(0)