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