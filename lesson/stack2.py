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
    def k(self):
        s=''
        for i in self.items:
            s=s+i
        return s
def parchecking(a):
    s=Stack()
    symbolstring=list(a)

    index=0
    while index < len(symbolstring) :
        if index==0:
            symbol = symbolstring[index]
            s.push(symbol)

        else:
            symbol = symbolstring[index]
            if  s.items==[]:
                s.push(symbol)

            else:
                if symbol==s.peek():
                    s.pop()
                else:
                    s.push(symbol)
        index=index+1



    if   s.isEmpty():
        return None
    else:
        return s.k()



print(parchecking(input()))