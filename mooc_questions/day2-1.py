def anagramSolution4(s1, s2):
    c1 = {}
    c2 = {}
    for char in s1:
        if char in c1:
            c1[char] += 1
        else:
            c1[char] = 1
    for char in s2:
        if char in c2:
            c2[char] += 1
        else:
            c2[char] = 1
    return c1 == c2


print(anagramSolution4('abc', 'abc'))

q=input()
t={}
for w in q:
    if w in  t:
        t[w]+=1
    else:
        t[w]=1
print(t)