# Queue
class Queue():
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item == []
    def enqueue(self,item):
        self.item.insert(0,item)
    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

q=Queue()
q.enqueue(3)
print(q.item)
q.dequeue()
print(q.item)
