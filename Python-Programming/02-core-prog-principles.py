
'''
types of variables
using variables
logical variables and oprators
while loop
for loop
if statement
random variables numpy.random.randn()
'''
a=1 # int
b='vivek' # string
c=True # bool
d=10.5 # floating point


# printing range - we need to use list
print(list(range(0,5)))

import numpy 
from numpy.random import randn
randn()

myString = "Hello, World!"
print (myString)

name = input('please enter your name')
print("hello ", name, ",how are you?")

age = input('please enter your age')
print('so you are', age, 'years old.')

# Types of variables 
v=True
print(type(v)) # Boolean / logical

str1 = "vivek"
len(str1)

str1 = "vivek"
str1[::-1]


# Working with Lists: - Can be of different variable types
# List is different from string because elements can be mutated/changed 
# Defining
L=[0,0,0] # [0, 0, 0]
L1=[0]*3 #shorthand way of defining a list with repeated elements

# Supports indexing and slicing
L1=['one', 'two', 'three']
L1[0] # 'one'
L1[1:2] # ['two'], upper bound is excluded
L1[1:3] # ['two', 'three']

# Indexing nested lists
L1 = ['one', 'two', ['three', 'four'], 'five']
L1[2][0] # 'three'

# Elements can be added
L1.append('six')

# Elements can be removed
L1.pop() # last element gets popped, we can save it in a variable also

# Sort
L1.sort() # sorts the list in-place, the actual list gets sorted
sorted(L1) #returns the sorted version of L3 list

# Reverse
L1=['c','a','b']
L1.reverse() # reverses the list in-place, the actual list gets reversed

# Multi dimentional list indexing
L1=[[1,2,3],[4,5,6],[7,8,9]]
L1[0][:] # returns first row

