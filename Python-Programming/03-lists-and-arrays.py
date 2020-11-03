
a=[]
a=range(1,10)
print(list(a))

# we can have mixed data types in a list
b=[1,2,3,'vivek',True,4,5]
print(list(b))

# index of list start with 0, 1, 2 ..
# so vivek is present at index 3
print(b[3])

# list can have a list as one of its elements

# slicing - [start:stop:step]
# slicing - [stop:start:-step] 
# end (stop) is not inclusive

# reversing a list
L[::-1]

# tuples - immutable list, cant be changed
t = (1,2,3) # use () instead of []

# module - group of functions
# packages - group of modules

# conda install package-name
# pip install package-name

# scrapy is a good web crawling package

# arrays
# python has inbuilt arrays and well as numpy arrays
# we just use numpy array as the inbuilt ones are less flexible
l=[546,375,254,651,781,569,454,564]

import numpy as np
a=np.array(l)
# if we convert a list with multiple data types (such as int, string, boolean, etc.)
# the numpy.array() function will convery all elements into a string, so it becomes an array of strings
# so data type of all elements in an array are same

print(a)

# when you slice an array you dont create a copy of an array
# so any modification to the slice of an array will be reflected in the actual array
a=[1,2,3,4]
a=np.array(a) # array([1, 2, 3, 4])
b=a[0:2]
b[:]=111 # array([1, 2])
# now, b becomes array([111, 111])
# but c also becomes array([111, 111,   3,   4])


# https://datatofish.com/
# Convert Strings to Integers in a Python List
# Using map
mylist = ['value1','value2','value3',...]
mylist = list(map(int, mylist))

# Using list comprehension
mylist = ['value1','value2','value3',...]
mylist = [int(i) for i in mylist]



