def getNum(s):
    res = 0
    for i in range(0, len(s), 3):
        if (s[i:i+3] == 'ONE'): 
            res = res * 10 + 1
        if (s[i:i+3] == 'TWO'): 
            res = res * 10 + 2
        if (s[i:i+3] == 'THR'): 
            res = res * 10 + 3
        if (s[i:i+3] == 'FOU'): 
            res = res * 10 + 4
        if (s[i:i+3] == 'FIV'): 
            res = res * 10 + 5
        if (s[i:i+3] == 'SIX'): 
            res = res * 10 + 6
        if (s[i:i+3] == 'SEV'): 
            res = res * 10 + 7
        if (s[i:i+3] == 'EIG'): 
            res = res * 10 + 8
        if (s[i:i+3] == 'NIN'): 
            res = res * 10 + 9
        if (s[i:i+3] == 'ZER'): 
            res = res * 10
    return res

def getString(n):
    res = ''
    while (n > 0):
        d = n % 10
        if (d == 1): res = 'ONE' + res
        if (d == 2): res = 'TWO' + res
        if (d == 3): res = 'THR' + res
        if (d == 4): res = 'FOU' + res
        if (d == 5): res = 'FIV' + res
        if (d == 6): res = 'SIX' + res
        if (d == 7): res = 'SEV' + res
        if (d == 8): res = 'EIG' + res
        if (d == 9): res = 'NIN' + res
        if (d == 0): res = 'ZER' + res
        n //= 10
    return res

s = input()
a = s[0: s.find('+')]
b = s[s.find('+') + 1: len(s)]
print(getString(getNum(a) + getNum(b)))