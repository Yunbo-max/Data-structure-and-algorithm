def id(y):
    x=str(y)[::-1]
    sum=0
    for each,i in zip(x,range(len(x))):
         sum+=int(each)*2**i%11
    return (sum%11)==1

print(id(input()))