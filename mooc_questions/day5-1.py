class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
def value(t):
    s = Queue()
    d=Queue()

    for i in range(len(t)):
        s.enqueue(t[i])

    j = ''
    for q in range(len(t)):
        j=j+s.items[q]
    print(j)
    for i in range(len(t)):
        s.enqueue(s.dequeue())

        k=''
        for w in range(len(t)):
            k=k+s.items[w]
        print(k)
        if k<j:
            j=k
        else:
            pass
    return j

t=eval(input())
print(value(t))
