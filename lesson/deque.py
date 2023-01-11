# from pythonds.basic.deque import  Deque
# def palcheker(string):
#     chardeque=Deque()
#     for ch in string:
#         chardeque.addRear(ch)
#     stillequal=True
#     while chardeque.size() > 1 and stillequal:
#         first=chardeque.removeFront()
#         last=chardeque.removeRear()
#         if first!=last:
#             stillequal= False
#     return stillequal
#
# print(palcheker("radar"))




def palcheker(string):
    a = string
    b = []
    j = 0
    balance = False
    for i in range(len(a)):
        b.append(a[i])
    while j<=len(a)/2:
        if b[j]==b[len(a)-j-1]:
            j = j+1
            balance = True
        else:
            balance = False
            break

    return balance


print(palcheker("radare"))