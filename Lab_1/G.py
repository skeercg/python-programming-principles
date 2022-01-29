def toDecimal(s, i):
    if (i == len(s)): return 0 
    else: return (pow(2, len(s) - i - 1) if s[i] == '1' else 0) + toDecimal(s, i + 1)

s = input()
print(toDecimal(s, 0))