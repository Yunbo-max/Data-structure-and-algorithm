
import random
import time
data_list = []

for i in range(1000000):

    data_list.append(random.randint(1,100))


#print("排序前列表：",data_list)

beginTime = time.time()

sorted(data_list)

#print("内置排序：", sorted(data_list))

endTime = time.time()

print("内置排序耗时：", endTime - beginTime)


beginTime = time.time()

merge_sort(data_list)

#print("排序后列表：", merge_sort(data_list))

endTime = time.time()

print("归并排序耗时：", endTime - beginTime)