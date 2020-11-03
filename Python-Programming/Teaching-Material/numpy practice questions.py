#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:18:44 2017

@author: vivekparashar
"""

# Try to run the following loop using arange function instead of range function
# for i in range(2,10,2):
#    print(i)
import numpy as np
for i in np.arange(2,10,2):
    print (i)


# Write a program that uses numpy array to generate the fibonacci sequence
import numpy as np
def fib_numpy(n):
    fib = np.zeros(n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[1:]


# Write a Python function to print all perfect numbers till 10,000
# first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
for i in range(10000):
    if perfect_number(i)==True:
        print (i)
        
        
# Write a Python program to sum and compute the product of a numpy array elements
# hint - sum() and prod() functions
import numpy as np
x = np.array([10, 20, 30], float)
print("Original array:")
print(x)
print("Sum of the array elements:")
print(x.sum())
print("Product of the array elements:")
print(x.prod())


# Write a Python program to count the frequency of unique values in numpy array
# hint - search for np.unique
import numpy as np
a = np.array( [10,10,20,10,20,20,20,30, 30,50,40,40] )
print("Original array:")
print(a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))


# Write a Python program to remove the negative values in a numpy array with 0.
import numpy as np
x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print("Original array:")
print(x)
print("Replace the negative values of the said array with 0:")
x[x < 0] = 0
print(x)


# Write a program to append two arrays
# hint - append function
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.append(a,b)




