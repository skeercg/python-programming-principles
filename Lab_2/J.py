n = int(input())
st = set()
for i in range(n):
    a = input()
    x = False
    y = False
    z = False
    for j in range(len(a)):
        if ('A' <= a[j] and a[j] <= 'Z'): x = True
        if ('a' <= a[j] and a[j] <= 'z'): y = True
        if ('0' <= a[j] and a[j] <= '9'): z = True
    if (x and y and z):
        st.add(a)
st = sorted(st)
print(len(st))
for i in st:
    print(i)