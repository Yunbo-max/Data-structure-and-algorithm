a=input()
c=[]
d=[']','}',')']
g=['[','{','(']

if len(a)%2 !=0:
    print('False')
else:
    for n in range(len(a)):
        c.append(a[n])

    for i in range(len(a)//2):
        for j in  [0,1,2]:
            if c[i]==g[j] and c[-i]==d[j]:
                print('True')
    if i==len(a)//2:
        print('False')






























