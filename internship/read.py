n=0
fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
    a=line.split()
    for i in range(len(a)):
        for j in range(len(lst)):
            if lst[j]==a[i]:
                n=1
        if n==0:
            lst.append(a[i])
        n=0
lst.sort()
print(lst)


