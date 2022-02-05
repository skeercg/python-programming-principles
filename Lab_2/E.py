n = list(map(int, input().split()))
x = int
if (len(n) == 2): x = n[1]
else: x = int(input())
a = []
for i in range(n[0]):
    a.append(x + 2 * i)
    if (i > 0): a[i] = a[i - 1] ^ a[i]
print(a[n[0] - 1])