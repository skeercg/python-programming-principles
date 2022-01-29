def isPrime(n):
    for i in range(2, n):
        if (n % i == 0): 
            return 0
    return 1

a, b = map(int, input().split())
if (b % 2 == 1):
    print('Try next time!')
elif (a <= 500 and isPrime(a)):
    print('Good job!')
else: print('Try next time!')