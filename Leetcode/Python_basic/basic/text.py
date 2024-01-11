import re
file=input()
text=open(file)
text2=text.read()
a=re.findall('[0-9]+',text2)
print(a)
sum=0
for i in a:
    sum=sum+int(i)
print(sum)