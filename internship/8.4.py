list = []
a = []
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    a = line.split()
    if a == None:
        continue
    else:

        if a[0] == "From":
            list.append(a[1])

b = dict()
for j in list:
    b[j] = b.get(j, 0) + 1

bigcount = None
bigword = None
for i, j in b.items():
    if bigword is None or j > bigcount:
        bigcount = j
        bigword = i
print(bigword, bigcount)