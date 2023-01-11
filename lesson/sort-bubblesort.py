def sortbubblesort(alist):
    exchange=True
    passnum=len(alist)-1
    while passnum>0 and exchange:
        exchange=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange=True
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
        passnum=passnum-1
alist=[20,30,40,90,50,60,70,80,100,110]
sortbubblesort(alist)
print(alist)