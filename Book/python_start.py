# bases
# 五种数据格式+输入输出+不同于错误的异常处理+面向对象(逻辑门电路+模拟森林火灾)+继承+鸭子接口
import numpy as np
s = np.random.uniform(-1,0,1000)
print(s.sum()/1000)

list = [2,3]
print(list*3)

# from numpy import array
# import matplotlib.pyplot as plt
# a = array([1,2,3,4])
# print(a)
# plt.plot(a,a**2)
# plt.show()
# print(12%5)
# a = 1+2j
# b = 2-1j
# print(a*b)
# import timeit
# timeit [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# from numpy import *
# import matplotlib.pyplot as plt
# # a = array()
# a = linspace(0,2*pi,21)
# b = sin(a)
# mask = b>=0
# # plt.plot(a,b)
# plt.plot(a[mask],b[mask],'ro')
# plt.show()
#
# print(type(a),type(b))
# print(a)


# def sum(a,b):
#     y=a+b
#     return y
#
# # a=[1.3,2.5,3,4]
# # b = [i for i in a]
# a = sum (3,4)
# print(a)

# class person():
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
#     def full_name(self):
#         return self.first+" "+self.last
#
# Person = person("yunbo","long",22)
# print(Person.full_name)
# # print(Person.first)


# url = 'http://ichart.finance.yahoo.com/table.csv?s=GE&d=10&e=5&f=2013&g=d&a=0&b=2&c=1962&ignore=.csv'
# import urllib2
# ge_csv = urllib2.urlopen(url)
# data = []
# for line in ge_csv:
#     data.append(line.split(','))
# data[:4]

# a = 2
# print(a << 3)
# from numpy import *
# from scipy.stats import norm
# import matplotlib.pyplot as plt
# x_norm = norm.rvs(size=500)
# type(x_norm)
# h = plt.hist(x_norm)
# x = linspace(-3,3,50)
# p = plt.plot(x, norm.pdf(x), 'r-')
# plt.show()
# print('counts, ', h[0])
# print('bin centers', h[1])
# x_mean, x_std = norm.fit(x_norm)
#
# print('mean, ', x_mean)
# print('x_std, ', x_std)

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# s = pd.Series([1,3,5,np.nan,6,8])
# a =np.random.randn(6,4)
# print(a)

#
# import datetime
# now = datetime.datetime.now()
# print("Last executed: " + now.strftime("%Y-%m-%d %H:%M:%S"))


# OOP
# import numpy as np
#
# class Forest(object):
#     """ Forest can grow trees which eventually die."""
#     def __init__(self, size=(150,150), p_sapling=0.0025, p_lightning=5.0e-6):
#         self.size = size
#         self.trees = np.zeros(self.size, dtype=bool)
#         self.fires = np.zeros((self.size), dtype=bool)
#         self.p_sapling = p_sapling
#         self.p_lightning = p_lightning
#
#     def __repr__(self):
#         my_repr = "{}(size={})".format(self.__class__.__name__, self.size)
#         return my_repr
#
#     def __str__(self):
#         return self.__class__.__name__
#
#     @property
#     def num_cells(self):
#         """Number of cells available for growing trees"""
#         return np.prod(self.size)
#
#     @property
#     def tree_fraction(self):
#         """
#  Fraction of trees
#  """
#         num_trees = self.trees.sum()
#         return float(num_trees) / self.num_cells
#
#     @property
#     def fire_fraction(self):
#         """
#  Fraction of fires
#  """
#         num_fires = self.fires.sum()
#         return float(num_fires) / self.num_cells
#
#     def _rand_bool(self, p):
#         """
#  Random boolean distributed according to p, less than p will be True
#  """
#         return np.random.uniform(size=self.trees.shape) < p
#
#     def grow_trees(self):
#         """
#  Growing trees.
#  """
#         growth_sites = self._rand_bool(self.p_sapling)
#         self.trees[growth_sites] = True
#
#     def start_fires(self):
#         """
#  Start of fire.
#  """
#         lightning_strikes = (self._rand_bool(self.p_lightning) &
#             self.trees)
#         self.fires[lightning_strikes] = True
#
#     def burn_trees(self):
#         """
#  Burn trees.
#  """
#         fires = np.zeros((self.size[0] + 2, self.size[1] + 2), dtype=bool)
#         fires[1:-1, 1:-1] = self.fires
#         north = fires[:-2, 1:-1]
#         south = fires[2:, 1:-1]
#         east = fires[1:-1, :-2]
#         west = fires[1:-1, 2:]
#         new_fires = (north | south | east | west) & self.trees
#         self.trees[self.fires] = False
#         self.fires = new_fires
#
#     def advance_one_step(self):
#         """
#  Advance one step
#  """
#         self.grow_trees()
#         self.start_fires()
#         self.burn_trees()
#
# import matplotlib.pyplot as plt
# from matplotlib import cm
# forest = Forest()
# forest2 = Forest(p_lightning=5e-4)
#
# tree_fractions = []
#
# for i in range(2500):
#     forest.advance_one_step()
#     forest2.advance_one_step()
#     tree_fractions.append((forest.tree_fraction, forest2.tree_fraction))
#
# plt.plot(tree_fractions)
#
# plt.show()


# for i in range(100):
#     forest.advance_one_step()
#     plt.matshow(forest.trees, cmap=cm.Greens)
#
#     plt.show()
