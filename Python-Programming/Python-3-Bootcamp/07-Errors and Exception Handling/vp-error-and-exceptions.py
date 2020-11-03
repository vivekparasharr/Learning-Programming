# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:25:31 2020

@author: vivek
"""

# try-except-else
try:
    result=10+'10'
except:
    print('error')
else:
    print(result)
    
   
# you can also catch for specific types of errors
try:
    f=open('testfile','r')
except TypeError:
    print('type error')
except OSError: # you can google more exception types
    print('os error')
finally:
    print('i always run')


# combine with while loop to ensure that we are handling exceptions properly
def ask_for_int():
    while True: #be careful using like this because we have to specifically break
        try:
            result=int(input('enter a number:'))
        except:
            print('not a number, try again')
            continue #this is added just to enhance readabillity
        else:
            print('thanks for entering a number')
            break
        finally:
            print('end of try-accept-finally')
            
    
# try-accept-finally to avoid zero division error
def zero_division_error():
    while True: #be careful using like this because we have to specifically break
        try:
            x=int(input('enter x:'))
            y=int(input('enter y:'))
            result=x/y
        except:
            print('zero division error, try again')
            continue #this is added just to enhance readabillity
        else:
            print('result of division is',result)
            break
        finally:
            print('all done!')
            
            
    
