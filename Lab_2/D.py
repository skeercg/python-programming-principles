n = int(input())
if (n % 2 == 1): 
    for i in range(n):
        for j in range(n):
            if (i + j + 1 < n): print('.', end = '')
            else: print('#', end = '')
        print()
else: 
    for i in range(n):
        for j in range(n):
            if (i < j): print('.', end = '')
            else: print('#', end = '')
        print()