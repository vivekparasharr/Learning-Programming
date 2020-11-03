# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:54:40 2020

@author: vivek
"""

# methods and funcitons 

# methods and the python documentation

l=[1,2,3]
l.append(4) #adds a last item, number 4

l.pop() #removes last item

help(l.insert)
l.insert(2,10) #inserts 10 on 2nd position


# introduction to functions
# allows to create a block of code that can be executed many times without needing to it write it again

def name_of_function(argument_name='default value'): #snake casing for name, all lower case alphabets with underscores
    '''
    what funciton does
    '''
    print ('hello',argument_name)
    print (f'hello {argument_name}') #both print do the same thing
    
    
def add_function(a=0,b=0):
    return a+b

# can call in the following two ways
# add_function(2,3)    
# c=add_function(3,4)


# logic with python function

def even_check (n=1):
    return n%2==0

def check_even_list (l):
    '''
    check if there is any even number in the list of numbers supplied
    '''
    for n in l:
        if n%2==0:
            return True
        else:
            pass #doesnt print False, but just breaks off the function
    return False


l_even=[]
def return_even_list (l):
    '''
    return all even number in the list of numbers supplied
    '''
    for n in l:
        if n%2==0:
            l_even.append(n)
        else:
            pass #doesnt print False, but just breaks off the function
    return l_even


# tuple unpacking with python funcitons

work_hours = [('james',100),('vivek',250),('bot',150)]
def unpack_tuple (work_hours):
    max_emp=''
    max_hrs=0
    for nm,hrs in work_hours:
        if hrs>max_hrs:
            max_hrs=hrs
            max_nm=nm
        else:
            pass
    return (max_nm,max_hrs)


# *args and **kwargs
# arguments and keyword arguments

# *args lets a function take an arbitrary number of arguments
# all arguments are received as a tuple, example - (a,b,c,..)
# wargs can be renamed to something else, what really matters is *

def myfunc(*args):
    return args
'''
myfunc(1,2,3,4,5,6,7,8,9)
Out[30]: (1, 2, 3, 4, 5, 6, 7, 8, 9)
'''

def myfunc(*args):
    for item in args:
        print(item)

# **kwargs lets the funciton take an arbitrary number of keyword arguments
# all arguments are received as a dictionary of key,value pairs
# kwargs can be renamed to something else, what really matters is **

def myfunc(**kwargs):
    print(kwargs)
'''
myfunc(name='vivek', age=34, height=186)
{'name': 'vivek', 'age': 34, 'height': 186}
'''    

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('i did not find any fruit here')


# make each alternate letter of a string uppercase
def myfunc(s):
    w=''
    for i in range(0,len(s)):
        print(i)
        if i%2==0:
            w=w+s[i].upper()
        else:
            w=w+s[i]
    return w
'''
myfunc('apple bottom jeans')
Out[43]: 'ApPlE BoTtOm jEaNs'
'''


# lambda functions, map funciton, filter function

# map
def square(n):
    return n**2

# if you have a list of numbers that you want to apply the square function to, something like [1,2,3,4]
l=[1,2,3,4]

# using traditional way
l2=[]
for i in range(0,len(l)):
    l2.append(square(l[i]))
print(l2)
'''
[1, 4, 9, 16]
'''

# MAP provides an alternate way to do this
list ( map (square,l) ) # when you pass square to map you dont pass as a function, just the funciton_name not function_name()
'''
Out[60]: [1, 4, 9, 16]
'''

#we can also iterate over this list to see each element
for i in map (square,l):
    print(i)
'''
1
4
9
16
'''


# LAMBDA expression

#traditional way for writing a square function
def square(a):
    print(a**2)

square(2)
'''
4
'''

# LAMBDA way
cube = lambda a: a**3 
#we write the input argument on the left of colon
#we write the return value on right of colon

cube(2)
'''
8
'''

#usually we wont assign the lambda to variable, like we did for cube
#instead we will use it in combination with MAP to apply over a list 

#example, return a list of cubes of all elements in the original list
lst=[1,2,3]
list ( map ( lambda a: a**3 , lst ) )
'''
Out[69]: [1, 8, 27]
'''

# FILTER function - basically if we are doing comparison in return section of lambda expression, we need to put that lambda expression in filter() instead of map()
# we can use lambda expression with filter function
# example, lets try to get all even numbers from a list
lst=[1,2,3,4,5,6,7,8,9]
list ( filter ( lambda a: a%2==0 , lst ) )


#example 2 - lets say you only want to return reverse of the strings in a list
lst=['andy','eve','sally']
list ( map ( lambda a: a[::-1], lst ) )


# GLOBAL VARIABLES
# how to use global variables in functions
x=50
print(x)

def func():
    global x #tells python to go to global space and grab the variable x from there
    #any changes to x will reflect to the global variable x
    #but, it better to use assignment operator with the funciton to modify a global variable, rather than using the global keyword
    x=200

func()
print(x)


