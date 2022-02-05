n = int(input())
a = list(map(int, input().split()))
mx = -9999
for x in range(n):
    for y in range(n):
        if (x != y): mx = max(mx, a[x] * a[y])
print(mx)