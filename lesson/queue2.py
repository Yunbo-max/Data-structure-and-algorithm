import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currenttask=None
        self.timeremaining=0
    def tick(self):
        if  self.currenttask !=None:
            self.timeremaining=self.timeremaining-1
            if self.timeremaining<=0:
                self.currenttask=None
    def busy(self):
        if self.currenttask!=None:
            return True
        else:
            return False
    def startnext(self,newtask):
        self.currenttask=newtask
        self.timeremaining=newtask.getpages()*60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getstamp(self):
        return self.timestamp
    def getpages(self):
        return self.pages
    def waittime(self,currenttime):
        return currenttime-self.timestamp

def newprinttask():
    num=random.randint(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numseconds,pagesperminute):
    labprinter=Printer(pagesperminute)
    printqueue=Queue()
    waitingtimes=[]
    for currentsecond in range(numseconds):
        if newprinttask():
            task=Task(currentsecond)
            printqueue.enqueue(task)
        if(not labprinter.busy())and (not printqueue.isEmpty()):
            nexttask=printqueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentsecond))
            labprinter.startnext(nexttask)
        labprinter.tick()
    averagewait=sum(waitingtimes)/len(waitingtimes)
    print("average wait %6.2f secs %3d tasks remaining."%(averagewait,printqueue.size()))

for i in range(10):
    simulation(3600,6)
