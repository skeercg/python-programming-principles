def gen(n):
    for i in range(0, n + 1):
        if (i % 12 == 0):
            yield i

n = int(input())

for i in gen(n):
    print(i)