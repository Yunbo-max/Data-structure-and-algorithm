a = input()
b = input()
c = a.split()
num = b.split()
j = 1
yushu = ''
zhuanhuan = ''
d = 0
e =[]
# print(num)
for i in range(len(num)):
    d = int(num[i])
    yushu = ''
    zhuanhuan = ''
    j = 1
    while j !=0:
        j = d//2
        yushu = str(int(d%2))
        zhuanhuan = yushu+zhuanhuan
        d = j
    e.append(zhuanhuan)
# print(e)

i = 0
for j in range(len(e)):
    i = int(32 - len(e[j]))
    e[j] = i*'0'+e[j]

# print(e)

start = int(c[1])
number = int(c[2])
f =[]
for i in e:
    f.append(i[(32-(start+number)):(32-(start))])

# print(f)
g = []
t = ''
h = []
for i in e:
    for j in f:
        g.append(i.split(j))
        # print(g)
        t = j+g[0][0]+g[0][1]
        h.append(t)
        # print(t)

k = []
# print(h)
for i in h:
    k.append(i[0:16])
# print(k)

sum = 0
l = []
for i in k:
    sum = 0
    for j in range(len(i)):
        if i[j] == '1':
            sum = sum + 2**(16-j-1)
    l.append(sum)

l = l[0:int(c[0])]
# print(l)
diction = dict(zip(l,[0]*len(l)))

for i in l:
    for key in diction:
        if i == key:
            diction[key] =  diction[key]+1

champion = True
check = []
for key in diction:
    check.append(diction[key])
# print(check)

m = 0
n =0
for i in range(len(check)):
    if m == 2:
        print(-1)
    if check[0] == check[i]:
        m = m+1
    else:
        n = max(check)
        for key in diction:
            if n == diction[key]:
                print(key)


