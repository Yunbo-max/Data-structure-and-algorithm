num = 100
result = []
str1 = ''
base = 7
r = num % base
num2 = int(num /base)
result.append(r)
while num2!=0:
    num = num2
    r = num %base
    num2 = int(num /base)
    result.append(r)

for i in range(len(result)):
    str1 = str(result[i]) + str1
print(result)
print(str1)
