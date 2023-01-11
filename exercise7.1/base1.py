class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    s=Stack()
    symbolstring=list(a)
    index=0
    while index < len(symbolstring) :




def Divide(a):
    b=[]
    c=[]
    for i in range(len(a)):
        if a[i]%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
    a=b+c
    return(a)

a = [1, 8, 3, 5, 6]
print(Divide(a))




