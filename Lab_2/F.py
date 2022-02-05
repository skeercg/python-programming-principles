n = int(input())
mp = {}
mx = -9999
for i in range(n):
    name, amount = input().split()
    if (name not in mp):
        mp[name] = int(amount)
    else: 
        mp[name] = mp[name] + int(amount)
    mx = max(mx, mp[name])
mp = mp.items()
mp = sorted(mp)
for i in mp:
    if (i[1] == mx):
        print(f'{i[0]} is lucky!')
    else: 
        print(f'{i[0]} has to receive {mx - i[1]} tenge')
