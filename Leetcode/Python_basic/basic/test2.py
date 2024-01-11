fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count=0
b=list()
fh = open(fname)
for line in fh:
    a=line.split()
    print(a)
    if a[0]=="From":
        b.append(a[1])
        count=count+1

for i in b:
    print(i)
print("There were", count, "lines in the file with From as the first word")
