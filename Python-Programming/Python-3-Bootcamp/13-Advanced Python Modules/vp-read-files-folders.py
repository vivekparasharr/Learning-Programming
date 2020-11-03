# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:50:31 2020

@author: vivek
"""

# current working directory
pwd
'''
Out[1]: 'C:\\Users\\vivek' #double back slash separator in windows, in mac/linux its forward slash
'''

# set working directory
import os
os.getcwd() # same as pwd, returns the current working directory
os.listdir() # lists everything in the current directory
os.listdir('c:\\Users') # lists everything in another directory
os.chdir('C:\\Users\\vivek\\OneDrive\\Documents\\GitHub\\vp_python_3_bootcamp\\13-Advanced Python Modules') # set current directory

f=open('practice.txt','w+')
f.write('this is a test string')
f.close()

# move a file
import shutil
shutil.move('practice.txt','C:\\Users\\vivek\\OneDrive\\Documents\\GitHub\\vp_python_3_bootcamp\\13-Advanced Python Modules\\test_folder')

# delete a file - 3 ways
os.unlink(path/file-name) # removes a file
os.rmdir(path) # removes a folder, but it needs to be empty before
shutil.rmtree(path) # removes a folder and all files in it

# alternate to os/shutil - doesnt permanatly delete, but sends to trash
# pipp install send2trash
import send2trash # this is a external module that does not delete, but sends to trash
send2trash.send2trash('practice.txt') # sends file to trash

# directory tree generator
os.walk(path) # returns a tuple
# tuple unpacking
for folder, sub_folder, files in os.walk('C:\\Users\\vivek\\OneDrive\\Documents\\GitHub\\vp_python_3_bootcamp\\13-Advanced Python Modules'):
    print(f'currently looking at {folder}')
    print('\nthe sub folders are: ')
    for sub_fold in sub_folder:
        print(f'\tsubfolder: {sub_fold}')
    print('\nthe files are: ')
    for file in files:
        print(f'\t\tfile: {file}')
# we can combine this with an if statement and get all text files starting with 2020 in a particular directory



        