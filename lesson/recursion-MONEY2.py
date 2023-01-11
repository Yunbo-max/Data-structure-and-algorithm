def dpmakechange(coinvaluelist,change,mincoins,coinused):
    for cents in range(change+1):
        coincount=cents
        newcoin=1
        for j in [c for c in coinvaluelist if c <=cents]:
            if  mincoins[cents-j]+1<coincount:
                coincount=mincoins[cents-j]+1
                newcoin=j
        mincoins[cents]=coincount
        coinused[cents]=newcoin
    return mincoins[change]

def printCoins(coinused,change):
    coin=change
    while coin>0:
        thisCoin=coinused[coin]
        print(thisCoin)
        coin=coin-thisCoin


import time

x=time.perf_counter()
a=[0]*64
b=[0]*64
print(dpmakechange([1,5,10,21,25],63,a,b),"coins")
printCoins(b,63)
print(b)
y=time.perf_counter()
print(y-x)





