def recdc(coinvaluelist,change,knownresults):
    mincoins=change
    if change in coinvaluelist:
        knownresults[change]=1
        return 1
    elif knownresults[change]>0:
        return knownresults[change]
    else:
        for i in [c for c in coinvaluelist if c<= change]:
            numcoins=1+recdc(coinvaluelist,change-i,knownresults)
            if numcoins<mincoins:
                mincoins=numcoins
                knownresults[change]=mincoins
    return mincoins

import time

a=time.perf_counter()
demo=[0]*64
print(recdc([1,5,10,25],2,demo))
b=time.perf_counter()
print(b-a)
print(demo)




