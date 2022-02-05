text = input().split()
st = set()
for word in text:
    for i in range(len(word)):
        if ('A' <= word[i] and word[i] <= 'Z'): True
        elif ('a' <= word[i] and word[i] <= 'z'): True
        else: word = word.replace(word[i], '')
    st.add(word)
st = sorted(st)
print(len(st))
for i in st:
    print(i)
