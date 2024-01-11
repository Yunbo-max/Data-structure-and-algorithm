# -*- coding = utf-8 -*-
# @time:03/09/2023 20:21
# Author:Yunbo Long
# @File:conjugation.py
# @Software:PyCharm


# sort的原因所以是logn的复杂度
# def conjugation(w1,w2):
#
#     list1=[]
#     list2=[]
#
#     for i in range(len(w1)):
#         list1.append(w1[i])
#
#     for i in range(len(w2)):
#         list2.append(w2[i])
#
#     list1.sort()
#     list2.sort()
#
#     i =0
#     test = True
#
#     for i in range(len(list1)):
#         if list1[i]==list2[i]:
#             i = i+1
#         else:
#             print('No Conjugation')
#             test = False
#             break
#
#     if test:
#         print('They are Conjugation')
#
# conjugation('wheel','leehw')

# n的复杂度，采用字典
# ord（‘a’）=97
# chr（‘97’）=a

def conjugation(w1,w2):



    alphabet_dict1 = {chr(97 + i): 0 for i in range(26)}
    # print(alphabet_dict1)
    alphabet_dict2 = {chr(97 + i): 0 for i in range(26)}
    # print(alphabet_dict1)

    for i in range(len(w1)):
        alphabet_dict1[w1[i]]=alphabet_dict1[w1[i]]+1

    for i in range(len(w2)):
        alphabet_dict2[w2[i]]=alphabet_dict2[w2[i]]+1

    if alphabet_dict1==alphabet_dict2:
        print('They are Conjugation')
    else:
        print('No Conjugation')

conjugation('wheel','leehw')


