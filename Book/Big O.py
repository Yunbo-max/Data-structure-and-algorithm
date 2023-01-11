# import time
# def sum_of_n_2(n):
#     start = time.time()
#     the_sum = 0
#     for i in range(1,n+1):
#         the_sum = the_sum + i
#         end =time.time()
#     return the_sum, end - start
#
#
# # def sum_of_n_3(n):
# #  return (n * (n +1)) / 2
#
#
# for i in range(5):
#     print('Sum is %d required %10.7f seconds' % sum_of_n_2(10000000))



import timeit
import random

lst1 = []
lst2 = []
for i in range(1000000, 10000001, 200000):
    x = list(range(i))
    t = timeit.Timer('del x[10]', 'from __main__ import x')

    lst_time = t.timeit(number=1)
    lst1.append(lst_time)

    x = {j: None for j in range(i)}
    t = timeit.Timer('del x[10]', 'from __main__ import x')

    d_time = t.timeit(number=1)
    lst2.append(d_time)

import matplotlib.pyplot as plt
print(lst1)

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.set_title('Time Complexity of del lst[i]/del dic[key]')
# plt.ylabel('Time')
# ax1.scatter(range(len(lst1)), lst1, s=8, c='b', label='del lst[i]')
# ax1.scatter(range(len(lst2)), lst2, s=5, c='red', marker='v', label='del dic[key]')
# plt.legend(loc='upper right')
plt.show()

import timeit
import random

lst1 = []
lst2 = []
for i in range(1000000, 10000001, 200000):
    x = list(range(i))
    lst_time = timeit.timeit('del x[10]','from __main__ import x',number=1)


    lst1.append(lst_time)

    x = {j: None for j in range(i)}
    d_time = timeit.timeit('del x[10]', 'from __main__ import x',number=1)


    lst2.append(d_time)

import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('Time Complexity of del lst[i]/del dic[key]')
plt.ylabel('Time')
ax1.scatter(range(len(lst1)), lst1, s=8, c='b', label='del lst[i]')
ax1.scatter(range(len(lst2)), lst2, s=5, c='red', marker='v', label='del dic[key]')
plt.legend(loc='upper right')
plt.show()