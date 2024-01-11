# from typing import List
#
#
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         # Sort the intervals
#         intervals.sort()
#
#         count = 0
#         i = 0
#
#         while (i < len(intervals) - 1):
#             if (intervals[i][1] > intervals[i + 1][0]):  # Check if end of current interval is greater than start of next interval
#                 count += 1
#
#                 # Remove the interval that has greater end value to ensure minimum removals
#                 if (intervals[i][1] > intervals[i + 1][1]):
#                     intervals.pop(i)
#                 else:
#                     intervals.pop(i + 1)
#             else:
#                 i += 1
#         return count
#
# a = Solution()
# b = [[1,2],[1,3],[2,4]]
#
# print(Solution.eraseOverlapIntervals([[1,2],[1,3],[2,4]]))

import operator
# -*- coding: utf-8 -*-
import operator
target_list = [[1,4],[2,3],[3,6]]
'''
sorted默认为从小到大排序，如果从大到小，请使用:
target_list.sort(key=operator.itemgetter(1), reverse=True) 
'''
target_list.sort(key=operator.itemgetter(1))
print(target_list)


target_list.sort(key=operator.itemgetter(1),reverse=True)
print(target_list)