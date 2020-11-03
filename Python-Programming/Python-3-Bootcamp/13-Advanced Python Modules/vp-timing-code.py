# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:49:43 2020

@author: vivek
"""

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str,range(n))) # map way is faster than list comprehension way

# method 1
import time
start_time=time.time() # current time before running code
result=func2(1000000)
end_time=time.time()
elapsed_time=end_time-start_time
print(elapsed_time)


# method 2
import timeit
statement='''
func1(100)
'''
setup='''
def func1(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(statement,setup,number=100000) # it will run func1 100,000 times to get a discernable difference


# method 3 - works with jupyter notebooks
%%timeit
func1(100)
# reports back - 100,000 loops, best of 3: 13.7 micro seconds per loop

