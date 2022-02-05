s = input()
q = []
f = True
for i in range(len(s)):
    if (s[i] == '(' or s[i] == '{' or s[i] == '['): 
        q.append(s[i])
    else:
        if (len(q) == 0):
            f = False
            break
        if (s[i] == ')'):
            if (q[len(q) - 1] != '('): f = False
            else: q.pop(len(q) - 1)
        if (s[i] == '}'):
            if (q[len(q) - 1] != '{'): f = False
            else: q.pop(len(q) - 1)
        if (s[i] == ']'):
            if (q[len(q) - 1] != '['): f = False
            else: q.pop(len(q) - 1)
if (f and len(q) == 0): print('Yes')
else: print('No')