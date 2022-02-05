n = int(input())
mp = {}
for i in range(n):
    a, b = input().split()
    if (b not in mp): 
        mp[b] = int(1)
    else: 
        mp[b] = mp[b] + int(1)
m = int(input())
for i in range(m):
    a, b, c = input().split()
    if (b in mp): 
        if (mp[b] > 0): 
            n = max(n - min(mp[b], int(c)), 0)
            if (int(c) > mp[b]): 
                mp[b] = 0
            else: 
                mp[b] = mp[b] - int(c)
print(f'Demons left: {n}')