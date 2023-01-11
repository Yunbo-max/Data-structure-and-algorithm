def first(num1,base1):
    s=0
    for i in range(len(num1)):

        s=(s+int(num1[i]))*int(base1)

    return int(s/int(base1))


def second(num,base):
    string="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num<base:
        return string[num]
    else:
        return second(num//base,base)+string[num%base]
a=input().split()

b=input()

t=0
t=first(b,a[0])
print(second(int(t),int(a[1])))

