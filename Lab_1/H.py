a = input()
b = input()
l = -1
r = -1
for i in range(len(a)):
    if (a[i] == b):
        l = i
        break
for i in reversed(range(len(a))):
    if (a[i] == b):
        r = i
        break
if (l != -1):
    if (l == r):
        print(l)
    else:
        print(l, r)