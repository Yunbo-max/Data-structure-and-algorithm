def repetition(s):
    a=list(s)
    x=[0]*len(a)

    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j]==a[i]:
                x[i]=x[i]+1
                x[j]=x[j]+1
    for k in range(len(x)):
        if x[k]==2:
            return a[k]

s='aab'
print(repetition(s))
t='abcacd'
print(repetition(t))