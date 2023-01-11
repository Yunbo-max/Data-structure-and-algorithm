a=[]
num=input()
for i in range(len(num)):
        a.append(int(num[i]))

t=False
b=[0,1,2,3,4,5,6,7,8,9]

for i in range(len(a)-1):
    if a[i+1]>a[i]:
        b[a[i]]=10
        t=True
    elif a[i+1]<a[i]:
        j=a[i]-1
        while j >=0:
            if  j in b and a[i+1]!=b[j]:
                t=False
                break



            elif  j in b and a[i+1]==b[j]:
                t=True
                b[a[i]]=10
                break

            j=j-1

    if t==False:
        break
if t== False:
    print('No')
else:
    print('Yes')







