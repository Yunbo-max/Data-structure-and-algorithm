def value(t):
    number=[]


    for j in t:
        a = 0
        for k in t:

            if k<=j and k>=j-10000 :
                a=a+1
        number.append(a)
    return number




t=eval(input())
print(value(t))