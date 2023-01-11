import re
text=''
file=open('yun.txt')
for line in file:
    text=text+line
file.close()
print(text)

pattern=r'136[0-9]{8}'
b='13691735318 213213213 213213 2132132131231'
print(re.sub(pattern,'1XXXXXXX',b))



