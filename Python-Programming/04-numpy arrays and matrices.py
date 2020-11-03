
# NumPy is often used along with packages like SciPy (Scientific Python) and Mat−plotlib (plotting library). This combination is widely used as a replacement for MatLab
# ndarray - an N-dimensional array; collection of items of the same type; items can be accessed using a zero-based index
# Each element in ndarray is an object of data-type object (called dtype)

import numpy as np 
a = np.array([1,2,3])  # [1, 2, 3]
a = np.array([[1, 2], [3, 4]]) 
'''
[[1, 2] 
 [3, 4]]
'''

# ndarray.shape - this array attribute returns a tuple consisting of array dimensions
a = np.array([[1,2,3],[4,5,6]]) 
print(a.shape) # (2, 3)

# It can also be used to resize the array
a.shape=(3,2)
'''
[[1, 2] 
 [3, 4] 
 [5, 6]]
'''

# NumPy also provides a reshape function to resize an array
a.reshape(3,2) 

a.ndim # 2 dimentional array

# numpy.linspace - this function is similar to arange() function. 
# In this function, instead of step size, the number of evenly spaced values between the interval is specified
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
x = np.linspace(10,20,5)  # [10.   12.5   15.   17.5  20.]

# numpy.logspace - this function returns an ndarray object that contains the numbers that are evenly spaced on a log scale. 
# Start and stop endpoints of the scale are indices of the base, usually 10.
# numpy.logspace(start, stop, num, endpoint, base, dtype)
# default base is 10 
a = np.logspace(1.0, 2.0, num = 10) 
'''
[ 10.           12.91549665     16.68100537      21.5443469  27.82559402      
  35.93813664   46.41588834     59.94842503      77.42636827    100.    ]
'''
a = np.logspace(1,10,num = 10, base = 2) 
# [ 2.     4.     8.    16.    32.    64.   128.   256.    512.   1024.] 


# arange funciton produces a list of numbers based on specifications
# numpy.arange(start, stop, step, dtype)
a=np.arange(8) # array([0, 1, 2, 3, 4, 5, 6, 7])
# now reshape it 
b = a.reshape(2,2,2) 
print(b) # b has three dimensions

b.dtype # its int32
b.itemsize

# specify data type
x = np.array([1,2,3,4,5], dtype = np.float32) 

'''
different data types
bool_ Boolean (True or False) stored as a byte
int_ Default integer type (same as C long; normally either int64 or int32)
intc Identical to C int (normally int32 or int64)
intp Integer used for indexing (same as C ssize_t; normally either int32 or int64)
int8 Byte (-128 to 127)
int16 Integer (-32768 to 32767)
int32 Integer (-2147483648 to 2147483647)
int64 Integer (-9223372036854775808 to 9223372036854775807)
uint8 Unsigned integer (0 to 255)
uint16 Unsigned integer (0 to 65535)
uint32 Unsigned integer (0 to 4294967295)
uint64 Unsigned integer (0 to 18446744073709551615)
float_ Shorthand for float64
float16 Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
float32 Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
float64 Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
complex_ Shorthand for complex128
complex64 Complex number, represented by two 32-bit floats (real and imaginary components)
complex128 Complex number, represented by two 64-bit floats (real and imaginary components)
'''


# numpy.empty creates an uninitialized array of specified shape and dtype
x = np.empty([3,2], dtype = int) 
print(x)
'''
[[ -572458896         495]
 [          0           0]
 [          1 -2147483648]]
Note − The elements in an array show random values as they are not initialized
'''

# numpy.zeros returns a new array of specified size, filled with zeros
x = np.zeros(5)  # array([0., 0., 0., 0., 0.])
x = np.zeros((5,), dtype = np.int)  # array([0, 0, 0, 0, 0])
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
'''
array([[(0, 0), (0, 0)],
       [(0, 0), (0, 0)]], dtype=[('x', '<i4'), ('y', '<i4')])
'''

# numpy.ones returns a new array of specified size and type, filled with ones
x = np.ones(5)  # array([1., 1., 1., 1., 1.])
x = np.ones([2,2], dtype = int) 
'''
array([[1, 1],
       [1, 1]])
'''


# numpy.asarray - this function is similar to numpy.array 
# # except for the fact that it has fewer parameters. 
# # This routine is useful for converting Python sequence into ndarray.

# convert list to ndarray
x = [1,2,3] 
a = np.asarray(x)

# dtype is set 
x = [1,2,3]
a = np.asarray(x, dtype = float) 

# ndarray from tuple 
x = (1,2,3) 
a = np.asarray(x) 

# ndarray from list of tuples 
x = [(1,2,3),(4,5)] 
a = np.asarray(x) 


# numpy.frombuffer - this function interprets a buffer as one-dimensional array. 
# Any object that exposes the buffer interface is used as parameter to return an ndarray.
s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 


# numpy.fromiter
# This function builds an ndarray object from any iterable object.
# A new one-dimensional array is returned by this function.
list = range(5) 
it = iter(list)   # obtain iterator object from list 
x = np.fromiter(it, dtype = float)   # use iterator to create ndarray 


# Slicing one dim array [start:stop:step<one-by-default>]
a = np.arange(10) 
slice(2,7,2)  # [2  4  6]
a[2:7:2]  # array([2, 4, 6])
a[2:7] # array([2, 3, 4, 5, 6])
a[5]  # 5 - this is just an individual int not an array
a[7:]  # array([7, 8, 9])

# Slicing two dim array
a = np.arange(9) 
a.shape=(3,3)
'''
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
'''
a[2,2] # 8
a[1,:]  # array([3, 4, 5]) - we can skip specifying :
a[:,1] # array([1, 4, 7]) - we cant skip specifying :
a[1:,:] # all columns of row 2 and 3 
'''
array([[3, 4, 5],
       [6, 7, 8]])
'''


# NaN (Not a Number) elements can be omitted by using ~ (complement operator)
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print(a[~np.isnan(a)]) # [1. 2. 3. 4. 5.]

# filter out the non-complex elements from an array
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print(a[np.iscomplex(a)]) # [2. +6.j 3.5+5.j]

'''
Broadcasting 
-Ability of NumPy to treat arrays of different shapes during arithmetic operations. 
-Arithmetic operations on arrays are usually done on corresponding elements. 
-If two arrays are of exactly the same shape, then these operations are smoothly performed.

Broadcasting is possible if the following rules are satisfied −
-Array with smaller ndim than the other is prepended with '1' in its shape.
-Size in each dimension of the output shape is maximum of the input sizes in that dimension.
-An input can be used in calculation, if its size in a particular dimension matches the output size or its value is exactly 1.
-If an input has a dimension size of 1, the first data entry in that dimension is used for all calculations along that dimension.

A set of arrays is said to be broadcastable if the above rules produce a valid result and one of the following is true −
-Arrays have exactly the same shape.
-Arrays have the same number of dimensions and the length of each dimension is either a common length or 1.
-Array having too few dimensions can have its shape prepended with a dimension of length 1, so that the above stated property is true.
'''
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
'''
First array:
[[ 0. 0. 0.]
 [ 10. 10. 10.]
 [ 20. 20. 20.]
 [ 30. 30. 30.]]

Second array:
[ 1. 2. 3.]

First Array + Second Array
[[ 1. 2. 3.]
 [ 11. 12. 13.]
 [ 21. 22. 23.]
 [ 31. 32. 33.]]
'''

# Iterating Over Array using numpy.nditer
a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a): # order of iteration is chosen to match the memory layout of the array (so transpose the array wont help, instead we can change the memory layout)
   print (x) # output 1

b = a.copy(order = 'F')  # we can change the memory layout of the array using order 
for x in np.nditer(b): 
   print (x) # output 2

for x in np.nditer(a, order = 'F'):  # or we can force nditer object to use a specific order by explicitly mentioning it
   print (x) # output 3
'''
Original array is:
[[ 0 5 10 15]
 [20 25 30 35]
 [40 45 50 55]]

Output 1:
0 5 10 15 20 25 30 35 40 45 50 55

Output 2:
0 20 40 5 25 45 10 30 50 15 35 55

Output 3:
0 20 40 5 25 45 10 30 50 15 35 55
'''


# Transposing an array
a=np.arange(9)
a.shape=(3,3)
a.T


# Modifying Array Values usinf op_flags parameter 
a = np.arange(0,60,5)
a = a.reshape(3,4)
print (a) # output 1
for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print(a) # output 2
'''
Output 1:
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]

Output 2:
[[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]]
'''


# extracting one-dimensional arrays corresponding to each column
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print(a)
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print(x)
'''
output 1:
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]

output 2:
[ 0 20 40]
[ 5 25 45]
[10 30 50]
[15 35 55]
'''

# Broadcasting Iteration
a = np.arange(0,60,5) 
a = a.reshape(3,4)
print(a) # output 1
b = np.array([1, 2, 3, 4], dtype = int) 
print(b) # output  2
for x,y in np.nditer([a,b]): 
   print(x+y) # output 3
'''
output 1:
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]

output 2:
[1 2 3 4]

output 3:
1 7 13 19 21 27 33 39 41 47 53 59
'''

# Array Manipulation
# Changing Shape
a = np.arange(8).reshape(2,4)  # reshape a 1x8 (1 row, 8 cols) array into a 2x4 array
a.flat[5] # 5 ; 1-D iterator over the array
a.flatten(order = 'F') # returns a copy of an array collapsed into one dimension
a.ravel(order = 'F') # Returns a contiguous flattened array / copy is made only if needed

# Transpose Operations
np.transpose(a) # same as a.T
a.T

# Changing Dimensions
a = np.arange(4).reshape(1,4)  # [0  1  2  3] 
np.broadcast_to(a,(4,4))
'''
[[0  1  2  3] 
 [0  1  2  3] 
 [0  1  2  3] 
 [0  1  2  3]]
'''

# Joining Arrays
a = np.array([[1,2],[3,4]]) 
'''First array:
[[1 2]
 [3 4]]'''
b = np.array([[5,6],[7,8]]) 
'''Second array:
[[5 6]
 [7 8]]'''

# concatenate joins a sequence of arrays along an existing axis
np.concatenate((a,b)) # by default it joins on axis=0, stacks horizontally - this is same as np.vstack((a,b)) 
'''Joining the two arrays along axis 0:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]'''
np.concatenate((a,b),axis = 1) # this is same as np.hstack((a,b))
'''Joining the two arrays along axis 1:
[[1 2 5 6]
 [3 4 7 8]]'''

# stack joins a sequence of arrays along a new axis
np.stack((a,b),0)
'''Stack the two arrays along axis 0:
[[[1 2]
 [3 4]]
 [[5 6]
 [7 8]]]'''
np.stack((a,b),1)
'''Stack the two arrays along axis 1:
[[[1 2]
 [5 6]]
 [[3 4]
 [7 8]]]''' 

# Splitting Arrays
a = np.arange(9) 
# [0 1 2 3 4 5 6 7 8]
np.split(a,3) # Split the array in 3 equal-sized subarrays:
# [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
np.split(a,[4,7]) # Split the array at positions indicated in 1-D array:
# [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]

a = np.arange(16).reshape(4,4)
'''
[[ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]
 [12 13 14 15]]'''
np.hsplit(a,2) # Horizontal splitting                                                        
'''[array([[ 0,  1],                                                             
       [ 4,  5],                                                              
       [ 8,  9],                                                              
       [12, 13]]), array([[ 2,  3],                                           
       [ 6,  7],                                                              
       [10, 11],                                                              
       [14, 15]])]'''
np.vsplit(a,2) # Vertical splitting                                                         
'''[array([[0, 1, 2, 3],                                                         
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],                               
       [12, 13, 14, 15]])]''' 

# Adding / Removing Elements
a = np.array([[1,2,3],[4,5,6]]) 
'''[[1 2 3]
 [4 5 6]]'''
np.resize(a,(3,3)) 
'''[[1 2 3]
 [4 5 6]
 [1 2 3]]''' # Observe that first row of a is repeated in b since size is bigger 


a = np.array([[1,2,3],[4,5,6]])
'''[[1 2 3]
 [4 5 6]]'''
np.append(a, [7,8,9])  # Append elements to array - Axis parameter not passed. The input array is flattened before append
# [1 2 3 4 5 6 7 8 9]
np.append(a, [[7,8,9]],axis = 0)  # Append elements along axis 0
'''[[1 2 3]
 [4 5 6]
 [7 8 9]]'''
np.append(a, [[5,5,5],[7,8,9]],axis = 1) # Append elements along axis 1
'''[[1 2 3 5 5 5]
 [4 5 6 7 8 9]]'''


a = np.array([[1,2],[3,4],[5,6]]) 
'''[[1 2]
 [3 4]
 [5 6]]'''
np.insert(a,3,[11,12])  # Axis parameter not passed. The input array is flattened before insertion.
# [ 1 2 3 11 12 4 5 6]
np.insert(a,1,[11],axis = 0)  # Broadcast along axis 0:
'''[[ 1 2]
 [11 11]
 [ 3 4]
 [ 5 6]]'''
np.insert(a,1,11,axis = 1) # Broadcast along axis 1:
'''[[ 1 11 2]
 [ 3 11 4]
 [ 5 11 6]]'''

a = np.arange(12).reshape(3,4) 
'''[[ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]]'''
np.delete(a,5)  # no axis specified, so array flattened before delete operation as axis not used
[ 0 1 2 3 4 6 7 8 9 10 11]
np.delete(a,1,axis = 1) # Column 2 deleted
'''[[ 0 2 3]
 [ 4 6 7]
 [ 8 10 11]]'''
np.delete(a, np.s_[::2]) # A slice containing alternate values from array deleted:
# [ 2 4 6 8 10]

# unique function returns an array of unique elements in the input array
a = np.array([5,2,6,2,7,5,6,8,2,9]) 
np.unique(a)  # Unique values of first array
u,indices = np.unique(a, return_index = True) # Unique array and Indices array
u[indices]  # Reconstruct the original array using indices
u,cnt = np.unique(a,return_counts = True) # Return the count of repetitions of unique elements


# Mathematical/statistical funcitons
a = np.array([1.0,5.55, 123, 0.567, 25.532])  
np.around(a)  # Default is 0. If negative, the integer is rounded to position to the left of the decimal point
np.around(a, decimals = 1)  # [   1.    5.6  123.    0.6  25.5] 
np.around(a, decimals = -1) # [   0.    10.  120.    0.   30. ]

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
np.floor(a) # [ -2.   1.  -1.   0.  10.]
np.ceil(a)  # [ -1.   2.  -0.   1.  10.]

# Arithmetic functions
a = np.arange(9, dtype = np.float_).reshape(3,3) 
'''[[ 0. 1. 2.]
 [ 3. 4. 5.]
 [ 6. 7. 8.]]'''
b = np.array([10,10,10])
# [10 10 10]
np.add(a,b) # Add the two arrays
[[ 10. 11. 12.]
 [ 13. 14. 15.]
 [ 16. 17. 18.]]
np.subtract(a,b) # Subtract the two arrays
[[-10. -9. -8.]
 [ -7. -6. -5.]
 [ -4. -3. -2.]]
np.multiply(a,b)  # Multiply the two arrays
[[ 0. 10. 20.]
 [ 30. 40. 50.]
 [ 60. 70. 80.]]
np.divide(a,b) # Divide the two arrays
[[ 0. 0.1 0.2]
 [ 0.3 0.4 0.5]
 [ 0.6 0.7 0.8]]

# Dot product
# For 2-D vectors, it is the equivalent to matrix multiplication. 
# For 1-D arrays, it is the inner product of the vectors. 
# For N-dimensional arrays, it is a sum product over the last axis of a and the second-last axis of b.
np.dot(a,b)
np.dot(b,a) == np.dot(a.T,b)


a=[1,2,3]
b=[2,3,1]
np.power(a,2) # array([1, 4, 9], dtype=int32)
np.power(a,b) # array([1, 8, 3], dtype=int32)

a = np.array([10,20,30]) 
b = np.array([3,5,7]) 
np.mod(a,b)  # same as np.remainder(a,b) 
# array([1, 0, 2], dtype=int32)

a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
np.amin(a,1)  # array of min in each row
np.amin(a,0)  # array of min in each col
np.amin(a)    # overall min element

# ptp function returns the range (maximum-minimum) of values along an axis
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
np.ptp(a)  
np.ptp(a, axis = 1) 
np.ptp(a, axis = 0) 

# Percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations fall
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 
np.percentile(a,50) 
# 50.0
np.percentile(a,50, axis = 1)  # 1 is rows
# [ 40. 20. 60.]  
np.percentile(a,50, axis = 0)  # 0 is columns
# [ 50. 40. 60.]

# Median is defined as the value separating the higher half of a data sample from the lower half
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
np.median(a) # 65.0
np.median(a, axis = 0)  # [ 50. 90. 60.]
np.median(a, axis = 1) # [ 65. 80. 60.]

# np.mean - syntax similar to np.median
# np.average function can be used to calculate weighted average if weights are specified, if they are not specified then this function is same as mean function
# In a multi-dimensional array, the axis for computation can be specified.
a = np.array([1,2,3,4]) 
np.average(a)
wts = np.array([4,3,2,1]) 
np.average(a,weights = wts) 

# Standard deviation is the square root of the average of squared deviations from mean
# std = sqrt(mean(abs(x - x.mean())**2))
np.std([1,2,3,4])

# Variance is the average of squared deviations - mean(abs(x - x.mean())**2)
# In other words, the standard deviation is the square root of variance
np.var([1,2,3,4])

# sorting
# sort() function returns a sorted copy of the input array
a = np.array([[3,7],[9,1]]) 
'''[[3 7]
 [9 1]]'''
np.sort(a) 
'''[[3 7]
 [1 9]]'''

# # Order parameter in sort function 
dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt) 
# [('raju', 21) ('anil', 25) ('ravi', 17) ('amar', 27)]
np.sort(a, order = 'name')
# [('amar', 27) ('anil', 25) ('raju', 21) ('ravi', 17)]

# numpy.argsort returns the array of indices of sorted array
# this indices array is used to construct the sorted array
x = np.array([3, 1, 2]) 
y = np.argsort(x)
x[y]  # Reconstruct original array in sorted order

# numpy.argmax() and numpy.argmin()
# return the indices of maximum and minimum elements along the given axis

# numpy.nonzero() function returns the indices of non-zero elements in the input array
# numpy.where(condition) function returns the indices of elements in an input array where the given condition is satisfied
# numpy.extract(condition) function returns the elements satisfying any condition

# id() returns a universal identifier of Python object, similar to the pointer in C
# While executing the functions, some of them return a copy of the input array, while some return the view
a
b=a # b.shape will also change the shape of a
# view - a different view of the same memory content 
b=a.view() # b.shape will not change the shape of a, even though both a and b have same id()
# copy - When the contents are physically stored in another location
b=a.copy() # b.shape will not change the shape of a, as a and b have different id()

# MATRIX
# matrix is always two-dimensional, whereas ndarray is an n-dimensional array. Both the objects are inter-convertible.
i = np.matrix('1,2;3,4') 
'''[[1  2] 
 [3  4]]'''
j = np.asarray(i) 
'''[[1  2] 
 [3  4]]'''
k = np.asmatrix (j) 
'''[[1  2] 
 [3  4]]'''

# Matrix functions
np.matlib.empty((2,2)) # returns a new matrix without initializing the entries (it will be filled with random data)
np.matlib.zeros((2,2)) # returns the matrix filled with zeros
np.matlib.ones((2,2))
np.matlib.eye(n = 3, M = 4, k = 0, dtype = float) # returns a matrix with 1 along the diagonal elements and the zeros elsewhere
np.matlib.identity(5, dtype = float) # returns the Identity matrix of the given size. An identity matrix is a square matrix with all diagonal elements as 1
np.matlib.rand(3,3) # returns a matrix of the given size filled with random values



