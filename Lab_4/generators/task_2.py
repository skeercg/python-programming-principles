def gen(n):
    for i in range(0, n + 1, 2):
        if (i + 2 >= n + 1):
            yield i
        else:
            yield f'{i},'

n = int(input())

for i in gen(n):
    print(i, end = ' ')