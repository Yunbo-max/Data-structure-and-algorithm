# -*- coding: utf-8 -*-
# @Author: Yunbo
# @Date:   2024-01-11 23:11:38
# @Last Modified by:   Yunbo
# @Last Modified time: 2024-02-15 22:43:25
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
