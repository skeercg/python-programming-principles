from math import sqrt

def dist(a, b, c, d):
    return sqrt(pow(a - c, 2) + pow(b - d, 2))

x, y = map(int, input().split())
n = int(input())
st = []
for i in range(n):
    a, b = map(int, input().split())
    st.append((dist(a, b, x, y), a, b))
st = sorted(st)
for i in st:
    print(i[1], i[2])