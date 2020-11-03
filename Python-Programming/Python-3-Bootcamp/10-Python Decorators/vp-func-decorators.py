# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:28:21 2020

@author: vivek
"""

# we can return fronction from a funciton and assign them to a variable name

def func():
    print('main func')
    def sub_func():
        print('sub func')
    return sub_func

'''
func()
main func
Out[99]: <function __main__.func.<locals>.sub_func()>

a=func()
main func

a()
sub func
'''

# we can pass function as an argument

def hello():
    return 'hello!'
 
def func(func_to_be_passed_as_argument):
    print('some random code')
    print(func_to_be_passed_as_argument())

'''
hello()
Out[107]: 'hello!'

func(hello)
some random code
hello!
'''

# using above two functionality we can create a decorator
def orig_func():
    print('hello there')
    
def new_decorator(original_func):
	def wrap_func():
		print('some extra code, before the original function')
		original_func()
		print('some extra code, after the original function')
	return wrap_func

'''
# way 1 for calling
new_decorator(orig_func)()
some extra code, before the original function
hello there
some extra code, after the original function

# way 2 for calling
a=new_decorator(orig_func)
a()
some extra code, before the original function
hello there
some extra code, after the original function
'''


# decorator way of doing it..
@new_decorator
def orig_func():
    print('hello there')

'''
orig_func()
some extra code, before the original function
hello there
some extra code, after the original function
'''


