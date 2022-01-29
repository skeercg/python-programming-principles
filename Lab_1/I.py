n = int(input())
for _ in range(n):
    a = input()
    if ('@gmail.com' in a):
        print(a.replace('@gmail.com', ''))