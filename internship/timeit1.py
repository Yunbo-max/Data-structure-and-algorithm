import timeit
import random
import matplotlib.pyplot as plt

lst1 = []
lst2 = []
lst3 = []
lst_time1=0
lst_time2=0
lst_time3=0

for i in range(1000000, 10000001, 200000):
    x1 = list(range(i))
    x2 = list(range(i))
    x3 = {j: None for j in range(i)}

    lst_time1 = timeit.timeit(stmt="x1.pop()", setup='from __main__ import x1', number=1)
    lst1.append(lst_time1)
    lst_time2 = timeit.timeit(stmt="x2.pop(0)", setup='from __main__ import x2', number=1)
    lst2.append(lst_time2)
    lst_time3 = timeit.timeit(stmt="del x3[0]", setup='from __main__ import x3', number=1)
    lst3.append(lst_time3)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('Time Complexity of del lst[i]/del dic[key]')
plt.ylabel('Time')
ax1.scatter(range(len(lst1)), lst1, s=8, c='b', label='pop()')
ax1.scatter(range(len(lst2)), lst2, s=5, c='red', marker='v', label='pop(0)')
ax1.scatter(range(len(lst3)), lst3, s=5, c='g', marker='v', label='del dictionary')
plt.legend(loc='upper right')
plt.show()