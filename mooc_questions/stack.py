# (((()))))问题
# a = input()
# b = {'(':0,')':0}
# for i in a:
#     if i == '(':
#         b['(']=b['(']+1
#     elif i == ')':
#         b[')']=b[')']+1
# if b['(']==b[')']:
#     print('True')
# else:
#     print('False')


#进制转化
# a = int(input())
# b = int(input())
# num2 = int(a/b)
# r = a%b
# c = []
# c.append(r)
# while num2!=0:
#     a = num2
#     num2 = int(a/b)
#     r = a%b
#     c.append(r)
#
# str1 = ''
# len = len(c)
# for i in range(len):
#     str1 = str1+str(c.pop())
#
#
# print(str1)

# a = input()
# b = {}
# c = [0]*len(a)
# d = [0] * len(a)
# e = []
#
# for i in range(len(a)):
#     c[i] = a[i]
#
#
# b = dict(zip(c,d))
#
# for j in range(len(a)):
#     b[a[j]] = b[a[j]]+1

# for key in b:
#     e.append(key)
#
# str1 = ''
#
# for i in range(len(e)):
#     str1 = str1 +e[i]
# print(str1)

a = input()
d = []
for i in range(len(a)):
    d.append(a[i])
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
c = []
balance = False
for i in range(len(b)):
    c.append(b[i].upper())
for j in range(len(a)):
    for i in range(len(b)):
        if a[j] == b[i] or a[j] == c[i]:
            balance = True
            continue
    if balance == False:
        d[j] = ' '
    balance = False
str1 = ''
for i in d:
    str1 = str1 +i
e = str1.split()
e.reverse()
str2 = ''
for i in e:
    str2 = str2 +i +' '

print(str2)
