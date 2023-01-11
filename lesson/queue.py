# from pythonds.basic.queue import Queue
# def hottomatoes(namelist,sum):
#     simqueue=Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#     while simqueue.size()>1:
#         for i in range(sum):
#             simqueue.enqueue(simqueue.dequeue())
#         simqueue.dequeue()
#     return simqueue.dequeue()
#
# print(hottomatoes(["long","suan","loun","sand"],2))

def potato(namelist,num):
    a = namelist
    b = []
    j = 1
    while len(a)>num:
        for i in range(1,len(a)+1):
            if j == num :
                a.pop()
                j = 1
            else:
                b.append(a.pop())
                a.insert(0,b[0])
                j = j+1
                b.pop()

    return a

print(potato(['long','wang','extend','sicsd','sadf'],2))
