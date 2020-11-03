#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:48:51 2017

@author: vivekparashar
"""

'defining fucntions
def add_numbers(x,y,z):
        return x+y+z

'using a user defined function

def add_numbers(x,y,z=None):
    if z==None:
        return x+y
    else:
        return x+y+z
    
add_numbers(1,2,3)
add_numbers(1,2)
a=add_numbers(1,2)
print a

x='this is a string'

print (x[-4:-1])

y=('chris','brooks','brooksch@unich.edu','vivek')
fname, lname, email=y
print (fname)


sales_record={'price': 3.24, 
              'num_items': 4, 
              'person': 'chris'}
sales_statement='{} bought {} item(s) at a price of {} each for a total of {}'
print(sales_statement.format(sales_record['person'],
						sales_record['num_items'],
						sales_record['price'],
						sales_record['num_items']*sales_record['price']))


import csv
%precision 2

#read csv
with open('/Users/vivekparashar/Documents/python dsp jupyter notebook/course1_downloads/mpg.csv') as csvfile:
    mpg=list(csv.DictReader(csvfile))

mpg[:3] #shows first 3 elements of the list

len(mpg) #length of the list

mpg[0].keys() #column names of the csv

sum(float(d['cty'])for d in mpg)/len(mpg) #avg city mpg across all cars in the csv file
#conversion to float was required because type of all values in our dictionary are strings 

sum(float(d['hwy'])for d in mpg)/len(mpg) #avg highway mpg across all cars in the csv file

# SUMMARIZE DATA THROUGH ITERATION   

#what the average city mpg is (grouped by number of cylinders the car has)
cylinders=set(d['cyl'] for d in mpg)   
cylinders

cty_mpg_by_cyl=[] #empty list where all calculations are stored
for c in cylinders: #first we iterate over all the cylinder levels
    sum_mpg=0
    cyl_typ_cnt=0
    for d in mpg: #then we iterate over all the dictionaries
        if d['cyl']==c: #if the cyl level for the dic where i am matches the cyl level we are calculating the avg for 
            sum_mpg+=float(d['cty']) #we add the mpg to our sum_mpg variable
            cyl_typ_cnt+=1 #and increment the count
    cty_mpg_by_cyl.append((c,sum_mpg/cyl_typ_cnt)) #after going through all the dictionaries we perform the avg mpg calc and append it to our list
    
cty_mpg_by_cyl.sort(key=lambda x:x[0]) #sort the list from lowest number of cyl to highest
cty_mpg_by_cyl            
                        
#find the average highway mpg for different vehicle classes            
vehicle_class=set(d['class'] for d in mpg)            
vehicle_class            
            
hwy_mpg_by_cls=[] #empty list where all calculations are stored
for c in vehicle_class: #first we iterate over all the cylinder levels
    sum_mpg=0
    cls_cnt=0
    for d in mpg: #then we iterate over all the dictionaries
        if d['class']==c: #if the cyl level for the dic where i am matches the cyl level we are calculating the avg for 
            sum_mpg+=float(d['hwy']) #we add the mpg to our sum_mpg variable
            cls_cnt+=1 #and increment the count
    hwy_mpg_by_cls.append((c,sum_mpg/cls_cnt)) #after going through all the dictionaries we perform the avg mpg calc and append it to our list
    
hwy_mpg_by_cls.sort(key=lambda x:x[1]) #sort the list from lowest number of cyl to highest
hwy_mpg_by_cls
            
            
import datetime as dt
import time as tm
tm.time() #you can get the current time since the epoch using the time module.            
dtnow=dt.datetime.fromtimestamp(tm.time()) #You can then create a time stamp using the from time stamp function on the date time object            
dtnow #When we print this value out, we see that the year, month, day, and so forth are also printed out           
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second            

datetime functions allow for simple math using time deltas
create a time delta of 100 days, then do subtraction and comparisons with the 
date time object. This is commonly used in data science for creating sliding 
windows. For instance, where you might want to look for any five day span of 
time where sales were highest, and flag that for follow up. 
            
delta=dt.timedelta(days=100)
delta            
            
today=dt.date.today()            
today #date today
today-delta #date 100 days before today           


#a class can be defined using the class keyword and ending with a colon
#anything indented below this is within the scope of the class
#classes are named using camel case, which means the first character of each word is capitalized
#you dont declare the variables within the object, you just start using them
#class variables can also be declaed, these are just variables which are shared across all instances
#objects in Python do not have private or protected members. If you instantiate an object, you have full access to any of the methods or attributes of that object
class Person: 
    department='school of informaition' 
    #Class variables can also be declared. These are just variables which are shared across all instances. So in this example, we're saying that the default for all people is at the school of information. 

    def set_name(self,new_name):
        self.name=new_name
    def set_location(self,new_location):
        self.location=new_location
#To define a method, you just write it as you would have a function. The one change, is that to have access to the instance which a method is being invoked upon, you must include self, in the method signature. 
#Similarly, if you want to refer to instance variables set on the object, you prepend them with the word self, with a full stop.         
#In this definition of a person, for instance, we have written two methods. Set name and set location. And both change instance bound variables, called name and location respectively. 
#When we run this cell, we see no output. The class exists, but we haven't created any objects yet. We can instantiate this class by calling the class name with empty parenthesis behind it. 
#Then we can call functions and print out attributes of the class using the dot notation, common in most languages. 
person=Person()
person.set_name('chris brooks')
person.set_location('ann arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


#Imagine we have two list of numbers, maybe prices from two different stores on exactly the same items. 
#And we wanted to find the minimum that we would have to pay if we bought the cheaper item between the 
#two stores. To do this, we could iterate through each list, comparing items and choosing the cheapest. 
#With map, we can do this comparison in a single statement. 

store1=[10.00,11.00,12.34,2.34]
store2=[9.00,11.10,12.34,2.01]
cheapest=map(min,store1,store2)
cheapest

#lazy evaluation. In Python, the map function returns to you a map object. 
#It doesn't actually try and run the function min on two items, until you look inside for a value. 
#This is an interesting design pattern of the language, and it's commonly used when dealing with big data. 
#This allows us to have very efficient memory management, even though something might be computationally complex. 
#Maps are iterable, just like lists and tuples, so we can use a for loop to look at all of the values in the map. 

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))

my_function=lambda a,b,c:a+b
my_function(1,2,3)



def times_tables():
    lst=[]
    for i in range(10):
        for j in range(10):
            lst.append(i*j)
    return lst




my_list=[]
for number in range(0,10):
	if number % 2 == 0:
		my_list.append(number)
my_list

my_list = [number for number in range(0,10) if number % 2 ==0]
my_list


lowercase='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'

#traditional approach
answer1=[]
for i in range(0,26):
    for j in range(0,26):
        for k in range(0,10):
            for l in range(0,10):
                answer1.append(lowercase[i]+lowercase[j]+digits[k]+digits[l])

#list comprehension approach
answer2=[lowercase[i]+lowercase[j]+digits[k]+digits[l] for i in range(0,26) for j in range(0,26) for k in range(0,10) for l in range(0,10)]

#even  better approach
answer3=[a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

#check
answer1==answer2
answer1==answer3


############### numpy ###############
#A package widely used in the data science commpunity which lets us work effeciently with arrays and metrices in python

import numpy as np #importing numpy as no. This lets us use the shotcut np to refer to numpy

#creating an array
mylist=[1,2,3] #create a list
x=np.array(mylist) #pass list to numpy to convert it to array
x

#we can also do this by passing the list to numpy directly
y=np.array([1,2,3])
y

#making multidimentional arrays by passing in a list of lists
#we pass 2 lists of 3 elements each and we get a 2x3 (2 by 3) array
m=np.array([[7,8,9],[10,11,12]])
m

#we can check the dimentions by using the shape attribute
m.shape

#for the arange function we pass in a start a stop and a step size
#and it returns you evenly spaced values within a given interval
n=np.arange(0,30,2)
n
#output: array([ 0,  2,  4, ..., 24, 26, 28])

#we can use reshape to convert this array of numbers into a 3x5 array
n=n.reshape(3,5)
n.shape
n
#output: 
array([[ 0,  2,  4,  6,  8],
       [10, 12, 14, 16, 18],
       [20, 22, 24, 26, 28]])

#linspace function is similar to arange, except we tell it how many numbers we want returned and it will split up the interval accordingly
#so we pass it a start a stop and how many numbers we want returned
o=np.linspace(0,4,9)
o
#output: array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ])

#resize can be used to change the dimentions in place
o.resize(3,3)
o
#output: 
array([[ 0. ,  0.5,  1. ],
       [ 1.5,  2. ,  2.5],
       [ 3. ,  3.5,  4. ]])
    
#difference between reshape and resize
ar = np.random.rand(2,3)
ar
ar.reshape(1,6)
ar #After reshape the array didn't change, but only outputs a temporary array reshape.
ar.resize(1,6)
ar #After resize the array changes it's shape

#numpy also has several built in functions and shortcuts for creating array
np.ones((3,2)) #returns a 3x2 array of ones
np.zeros((2,3)) #returns a 2x3 array of zeros
np.eye(3) #returns a 3x3 array with ones on the diagonal and zeros everywhere else 

y=np.array([1,2,3])
np.diag(y)      
#output
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
    
#to create an array with repeated values we can pass in a repeated list, or we can use numpy's repeat function
np.array([1,2,3]*3)  #output: array([1, 2, 3, 1, 2, 3, 1, 2, 3])
np.repeat([1,2,3],3) #output: array([1, 1, 1, 2, 2, 2, 3, 3, 3])    
#notice difference between the two outputs     
    
#we can also combine arrays to create new ones
#lets create a 2x3 array of ones 
p=np.ones([2,3],int)
p
#output
array([[1, 1, 1],
       [1, 1, 1]])
    
#and stack it vertically with itself multiplied by 2
np.vstack([p,2*p])   
#output
array([[1, 1, 1],
       [1, 1, 1],
       [2, 2, 2],
       [2, 2, 2]])

#now lets stack horizontally
np.hstack([p,2*p]) 
#outpput
array([[1, 1, 1, 2, 2, 2],
       [1, 1, 1, 2, 2, 2]])
    
#operations that can be done with numpy arrays
#element wise +,-,*,/
x=np.array([1,2,3])
y=np.array([4,5,6])
x+y
x*y

#x to the power 2 (this is also element wize)
x**2    
    
#linear algebra dot product can be done using the dot function
x.dot(y)    

#lets create a new array using the previous array y and its squared values
y=np.array([4,5,6])
z=np.array([y,y**2])
#output
array([[ 4,  5,  6],
       [16, 25, 36]])
#the shape of this array is 2x3 (2  by 3)

#transposing an array using the t method which swaps the rows and columns
z.T
#output:
array([[ 4, 16],
       [ 5, 25],
       [ 6, 36]])    
#the shape of the transposed array is 3x2

z.dtype #we can see the type of data the array has

z=z.astype('f') #casting and array to a different type, from int64 to float32 in this case
z.dtype 

#commonly used math functions
a=np.array([-4,-2,1,3,5])
a.sum()
a.max()
a.min()
a.mean() #mean of all the values
a.std() #standard deviation of all the values
a.argmax() #index of the maximum value
a.argmin() #index of the minimum value  

####        
#indexing and slicing
#create array of squares of 0-12
s=np.arange(13)**2

#we can use [] notation to get the value at a particular index
s[4] #output: 16
#and the column notation to get a range
#notation is starting index, ending index and step size
#specifying the staring or ending index is not necessary
#we can also use negatives to count back from the end of the array
s[0:3] #output: array([0, 1, 4])           

s[1:5] #range starting from index 1 and stopping before index 5
s[-4:] #slice of last 4 elements of the arrau
s[-5::-2] #starting 5th from the end to the begenning of the array and counting backwards by 2

####
#lets see how this extends to a 2 dimentional arry
#lets create a 2 dimentional array from 0-35 and resize it as 6x6
r=np.arange(36)
r.resize((6,6))
#output:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])

r[2,2] #14 is the value at second row second column
r[3,3:6] #colon notation used to get a slice of 3rd row column 3-6
r[:2,:-1] #first two rows and all the columns except the last 
r[-1,::2] #select every second element from the last row 
r[r>30] #use bracket operator to do conditional indexing and assignment
r[r>30]=30 #capping the max value of elements in the array to 30
#output:
    array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 30, 30, 30, 30, 30]])
    

#copying data
#first lets create a new array r2 which is the slice of the array r
r2=r[:3,:3]
#output
array([[ 0,  1,  2],
       [ 6,  7,  8],
       [12, 13, 14]])

r2[:]=0 #sets all elements of this array to 0
#now if we look at the original array r, we see that the slice of data in the original array has also been changed
#this is something to keep in mind and be careful about when working with numpy arrays
#output:
    array([[ 0,  0,  0,  3,  4,  5],
       [ 0,  0,  0,  9, 10, 11],
       [ 0,  0,  0, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 30, 30, 30, 30, 30]])

#copy can be used to avoid this
r_copy=r.copy()
r_copy
r_copy[:]=10
      
print (r)
print (r_copy)


#iterating over arrays
#first lets create a 4x3 array of random nubers from 0-9
test=np.random.randint(0,10,(4,3))
print(test)

#iterate by row
for row in test :
    print (row)
    
#iterate by row index using the length function on test which returns the number of rows
for i in range(len(test)):
    print (test[i])
    
#we can combines these two ways of iterating by using enumerate, which gives us the row and the index of the row
for i,row in enumerate(test):
    print('row',i,'is',row)      

#zip
test2=test**2
print(test2)
#if we wish to iterate throughboth arrays we can use zip
for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)


############### pandas ###############

import pandas as pd 

#Ask for help
pd.Series? 
    
#You can create a series by passing in a list of values
#When you do this, pandas automatically assigns an index starting with 0 and sets the name of the series as none

animals=['tiger','bear','moose']
pd.Series(animals)
Out[237]: 
0    tiger
1     bear
2    moose
dtype: object

#Pandas automatically identified the type of data eing held in the list
#in this case we passed in a list of strings and pandas set the type to object

numbers=[1,2,3]
pd.Series(numbers)
Out[238]: 
0    1
1    2
2    3
dtype: int64

#Underneath panda stores series values in a typed array using the numpy library. 
#This offers significant speed-up when processing data versus traditional python lists. 


#how numpy and thus pandas handle missing data. 
#In Python, we have the none type to indicate a lack of data. 
#But what do we do if we want to have a typed list like we do in the series object? 

animals=['tiger','bear',None]
pd.Series(animals)
Out[240]: 
0    tiger
1     bear
2     None
dtype: object

numbers=[1,2,None]
pd.Series(numbers)
Out[241]: 
0    1.0
1    2.0
2    NaN #pandas automatically converts this to a special floating point value designated as NaN, which stands for not a number
dtype: float64

np.NaN==None #NaN is not None and when we try the equality test, it's false.
np.NaN==np.NaN #can't do an equality test of NaN to itself either

np.isnan(np.NaN) #this function is used to test for the presence of not a number

        
# series can be created from dictionary data. 
#If you do this, the index is automatically assigned to the keys of the dictionary 
#that you provided and not just incrementing integers        
        
import pandas as pd
sports={'archery':'bhutan','golf':'scotland','sumo':'japan','taekwondo':'south korea'}
print(sports)
s=pd.Series(sports)
print(s)




#line chart
import matplotlib.pyplot as plt
plt.plot([1,2,3],[5,7,4])
plt.show()

#line chart
import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
plt.plot(x,y)
plt.xlabel('Plot number')
plt.ylabel('Important variable\nBut what is it')
plt.title('Interesting graph\nCheck it out')
plt.show()



#line chart
import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y,label='first series')
plt.plot(x2,y2,label='second series')
plt.xlabel('plot number')
plt.ylabel('important variable\nBut what is it')
plt.title('interesting graph\nCheck it out')
plt.legend()
plt.show()



#bar chart
import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
plt.bar(x,y,label='bars1',color='r')
plt.bar(x2,y2,label='bars2',color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()


#histogram
import matplotlib.pyplot as plt
population_ages=[22,55,62,45,21,22,34,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
#following two comments help compare a histogram vs a bar chart for the same data
#ids=[x for x in range(len(population_ages))]
#plt.bar(ids,population_ages,label='bars1')
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130] 
#bin 0 has all values from 0-9, bin 10 has all values from 10-19 etc.
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()


#scatter plot
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y,label='skitscat',color='k',marker='*',s=200)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()



#stack plot
import matplotlib.pyplot as plt

days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='b',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)
plt.stackplot(days, sleeping,eating,working,playing, colors=['b','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()



#pie chart
import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

slices=[7,2,2,13] #slice of day 5
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices, labels=activities, colors=cols, startangle=90
        , explode=(0,0.1,0,0), autopct='%1.1f%%')
#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
#plt.legend()
plt.show()





#loading data from files using csv
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('example.txt','r') as csvfile:
        plots=csv.reader(csvfile,delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
            
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()


#loading data from files using numpy
import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)
            
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()




#loading data from internet using yahoo api
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

from matplotlib.dates import bytespdate2num

def bytespdate2num(fmt,encoding='utf-8'):
    strconverter=mdates.strpdate2num(fmt) #strip dates to number
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    stock_price_url='https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code=urllib.request.urlopen(stock_price_url).read()
    stock_data=[]
    split_source=source_code.split('\n')
    for line in split_source:
        split_line=line.split(',')
        if len(split_line)==6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date,closep,highp,lowp,openp,volume=np.loadtxt(stock_data,
                                                   delimiter=',',
                                                   unpack=True,
                                                   #%Y = full year. 2015
                                                   #%y = partial yr. 15
                                                   #%m = month number
                                                   #%d = day number
                                                   #%H = hours
                                                   #%M = minutes
                                                   #%S = seconds
                                                   #%m-%d-%Y = 12-06-2014
                                                   converters={0:bytespdate2num('%Y%m%d')}) # matplot lib doesnt use unix time, it has its own conversion  
plt.plot_date(date,closep)

plt.xlabel('date')
plt.ylabel('close_price')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()

graph_data('TSLA')




from yahoo_finance import Share
yahoo = Share('YHOO')

yahoo.get_open()
yahoo.get_price()
yahoo.get_trade_datetime()
yahoo.refresh() #Refresh data from market
yahoo.get_historical('2014-04-25', '2014-04-29')

from yahoo_finance import Currency
eur_pln = Currency('EURPLN')
eur_pln.get_bid()
eur_pln.get_ask()
eur_pln.get_rate()
eur_pln.get_trade_datetime()
eur_pln.refresh()


#reading google finance data
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f = web.DataReader("F", 'google', start, end)
f.ix['2010-01-04']

#reading yahoo finance data
#not working
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f = web.DataReader("F", 'yahoo', start, end)
f.ix['2010-01-04']




gticker='NASDAQ:TSLA'
import pandas_datareader as web
dfg = web.DataReader(gticker, 'google', '2015/4/24', '2016/4/28')

dfg #returned pandas dataframe
sa=dfg.reset_index().values #convert pandas dataframe to numpy array

#accessing dataframe                  
dfg.loc[:,['Volume']]
dfg.iloc[:,[4]]

dfg.index.dtype #dtype of index

dfg.columns.tolist() #enlists column names

import matplotlib.pyplot as plt
dfg.boxplot(column="Open",by="High") #box plot of data from pandas dataframe

plt.plot(sa[:,0],sa[:,2:3],label='High')
plt.plot(sa[:,0],sa[:,3:4],label='Low')
plt.legend()

plt.bar(sa[:,0],sa[:,2:3],label='High')

bins=[140,145,150,155,160,165,170,175,180,185,190] 
plt.hist(sa[:,2:3],bins,histtype='bar',rwidth=0.8) #define bins yourself
plt.hist(sa[:,2:3],bins=20,histtype='bar',rwidth=0.8) #just tell the number of bins

plt.scatter(sa[:,1:2],sa[:,2:3]) #scatter plot of data, using data from structured array


#tutorial 8-9            
import matplotlib.pyplot as plt
plt.plot(sa[:,0],sa[:,2:3],label='High')
plt.plot(sa[:,0],sa[:,3:4],label='Low')
plt.legend()

#tutorial 10
fig=plt.figure()
ax1=plt.subplot2grid((1,1), (0,0)) #first axis
ax1.plot(sa[:,0],sa[:,2:3],label='High') #this is a sub plot

#plt.yscale('log') #to convery y axis to log scale
plt.minorticks_on() #turn minor tick marks on. this is needed to plot minor lines
ax1.grid(True,color='g',which='major',linestyle='-',linewidth=2) #which can be major , minor, both
ax1.grid(True,color='g',which='minor',linestyle='-') #which can be major , minor, both

#to rotate labels
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
        
plt.xlabel('Date')
plt.ylabel('High Price')
plt.legend()
plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.90,wspace=0.2,hspace=10)
plt.show()


#figure
#axes
#data
#everything that goes on to your each individual sub plot which is your axes
#at the bottom all plt stuff thats gonna apply to all the graphs





           