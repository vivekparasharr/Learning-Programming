# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:36:16 2020

@author: vivek
"""

# creating pandas dataframe
import pandas as pd
# From dict
pd.DataFrame({'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']})
# from list
pd.DataFrame(['orange', 'mango', 'grapes', 'apple'], index=['a', 'b', 'c', 'd'], columns =['Fruits'])
# from list of lists
pd.DataFrame([['orange','tomato'],['mango','potato'],['grapes','onion'],['apple','chilly']], index=['a', 'b', 'c', 'd'], columns =['Fruits', 'Vegetables'])
# from multiple lists
pd.DataFrame(
        list(zip(['orange', 'mango', 'grapes', 'apple'],
                ['tomato', 'potato', 'onion', 'chilly']))
        , index=['a', 'b', 'c', 'd']
        , columns =['Fruits', 'Vegetables'])

#################################################################################
################################### summary #####################################
#################################################################################

# get the values of a dataframe (not the column nmaes or row names)
df.values 


# type conversion
# if we have year and we want to convery it from int to category
from os import SF_NODISKIO


df.col1 = df.col1.astype('category')
# Get unique values in a category
df.col1.cat.categories
df.col1.unique()


# \ - can be put at end of line to continue writing code in next line

df.copy()

df.drop_duplicates()

#Initialize DataFrame
#From list-of-lists: 
df=pd.DataFrame(list-of-lists, columns =['Name', 'Age']) 
#From different lists: 
df=pd.DataFrame(list(zip(l1,l2,..)), columns=[‘c1’,’c2’,..])
#From np-array: 
df=pd.DataFrame(data=np-array, index=[‘r1’,’r2’,..], columns=[‘c1’,’c2’,..])
#From dict: 
df=pd.DataFrame({‘c1’: [data,data,..],’c2’: [data,data,..],..})
#From csv: 
df=pd.read_csv(‘file.csv')
#From excel: 
df=pd.read_excel(’file.xlsx')  # pip install xlrd

#Export df
df.to_csv(‘file.csv', index = False, header=True)


.shape, .side, .ndim, .columns, df[‘c1’].value_counts()
len(df.columns)

.info(), .describe(), .transpose(), .head(), .tail()
.count(), .mean(skipna=False), .sd(), .min(), .quantile(q=0.25), .max()
.unique(), .nunique()
.sum(axis=0) # 1 for row sum
.value_counts() - 

# Drop a row or col 
df.drop('another_col',axis=1) # drop col another_col
df.drop(2, axis=0) # drop row 2

# isin
df[df.country.isin(['CN','IN'])] # rows where country in ('CN','IN') returned
df[~df.country.isin(['CN','IN'])] # rows where country not in ('CN','IN') returned

#Add a column to df
df['new_col'] = res
df['another_col'] = pd.DataFrame(np.arange(0,195))
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]

# query a dataframe
df_filtered = df.query('a > 1 & b > 1')

#Add a column based on conditions
# IF condition
df.loc[df.column_name condition, ‘new column name’] = ‘value if condition is met’
df.loc[df.set_of_numbers <= 4, 'equal_or_lower_than_4?'] = 'True' 
df.loc[df.set_of_numbers > 4, 'equal_or_lower_than_4?'] = 'False' 

df.loc[(df.First_name == 'Bill') | (df.First_name == 'Emma'), 'name_match'] = 'Match'  # multiple conditions can be specified using logical operators

# NUMPY way
np.where(condition, value if condition is true, value if condition is false)
df['Good'] = np.where(df['points']>20, 'yes', 'no')  # New Column with Binary Values

# Create a New Column Based on Comparison with Existing Column
df['assist_more'] = np.where(df['assists']>df['rebounds'], 'yes', 'no')

# New Column with Multiple Values using np.select
# create a list of our conditions
conditions = [
    (df['likes_count'] <= 2),
    (df['likes_count'] > 2) & (df['likes_count'] <= 9),
    (df['likes_count'] > 9) & (df['likes_count'] <= 15),
    (df['likes_count'] > 15)
    ]
# create a list of the values we want to assign for each condition
values = ['tier_4', 'tier_3', 'tier_2', 'tier_1']
# create a new column and use np.select to assign values to it using our lists as arguments
df['tier'] = np.select(conditions, values)

# New Column with Multiple Values
def f(row):
    if row['points'] < 15:
        val = 'no'
    elif row['points'] < 25:
        val = 'maybe'
    else:
        val = 'yes'
    return val
#create new column 'Good' using the function above
df['Good'] = df.apply(f, axis=1)

# PANDAS way
# we don’t have to rely on NumPy to create new column using condition on another column. Instead we can use Panda’s apply function with lambda function.
df[‘new column name‘] = df[‘df column_name‘].apply(lambda x: ‘value if condition is met’  if x condition else ‘value if condition is not met’)

gapminder['gdpPercap_ind'] = gapminder.gdpPercap.apply(lambda x: 1 if x >= 1000 else 0)

# we can create complex conditionals as well
gapminder['continent_group'] = gapminder.continent.apply(lambda x: 1 if x in ['Europe','America', 'Oceania'] else 0)

# another example of .apply
def set_values(row, value):
    return value[row]
map_dictionary ={200 : "Low", 300 :"LOW", 400 : "MID",500:"HIGH",600:"HIGH"} 
df['Salary_Range'] = df['Salary'].apply(set_values, args =(map_dictionary, )) 

DataFrame.apply(self, 
                func, 
                axis=0, # axis=1 or axis = 'columns'
                raw=False, 
                result_type=None, 
                args=(), 
                **kwds)

# another pandas way is to use .map
map_dictionary ={200 : "Low", 300 :"LOW", 400 : "MID",500:"HIGH",600:"HIGH"} 
df['Salary_Range'] = df['Salary'].map(map_dictionary) 


#Subsetting - data.loc[<row selection>, <column selection>]
df[‘col-name’] # by col name
df[[‘col-name’]] 

.loc[ [row-names] , [col-names] ] # by row/col names
.loc[cond1 & cond2 | cond3 ^ ~(cond4)] 

.iloc[ [row-numbers] , [col-numbers] ] # by row/col numbers
df.iloc[[0,3], [0,2]] # 1st, 4th row and 1st, 3rd columns
df.iloc[0:2, 1:4] # first 2 rows and 2nd, 3rd, 4th columns of data frame

#Get specific values in rows/cols
df.iat[0,0]
df.at[0,'CountryName'] # incidently row label is an integer in this case so we specify without quotes


#String operations
s.shelter_city.str.upper() # lower, strip, startswith('char'), endswith, get_dummies, len, contains(‘text’)
s.shelter_address.str.split(' ').str[1]
s2=s.shelter_address.str.split(' ', expand=True) # with expand=True, returns a df, else a list
s2.iloc[:,1].str.cat(s2.iloc[:,2], sep=', ')
# col1.str.cat(col2, sep=', ')

#Numeric operations
df.c1 + df.c2 # all arithmetic operations possible


.groupby([‘c1’,’c2’,..]).sum()[‘c4’] # sum of 4th column
 .get_group(2014) # we can select a single group
 .agg(np.mean) # average
 .agg([np.sum, np.mean, np.std])

df.apply(np.sum, axis=0)  # to columns
df.apply(np.sum, axis=1) # to rows


.shift() Series method


#################################################################################
#################################### pivot ######################################
#################################################################################

import seaborn as sns 

# use seaborn datasets
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.info

# three ways
df.pivot_table(index='sex', columns='alive', values='age')
pd.crosstab(index=df.sex, columns=df.alive, values=df.age, aggfunc='mean', normalize=True) # transforms the values as percentages (by default it is % of total dataset, but we can change it to % of row or column)
df.groupby(['sex','alive']).mean()['age'].unstack() # unstack grabs outermost index (from sex and alive, it is alive) and moves it to columns


#################################################################################
################################### detailed ####################################
#################################################################################


import numpy as np
import pandas as pd
# import seaborn as sns

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

# creating a copy of the dataframe
df2 = df1.copy()

 
##### Importing or creating data

# create artificial data
# from lists
lst = [['tom', 25], ['krish', 30], 
       ['nick', 26], ['juli', 22]] 
df = pd.DataFrame(lst, columns =['Name', 'Age']) 

# 2 different lists
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
lst2 = [11, 22, 33, 44, 55, 66, 77] 
df = pd.DataFrame(list(zip(lst, lst2)), 
               columns =['Name', 'val'])

# from np.array
columns = ["A", "B", "C"]
rows = ["D", "E", "F"]
data = np.array([[1, 2, 2], [3, 3, 3],[4, 4, 4]])
df = pd.DataFrame(data=data, index=rows, columns=columns)

# from dict
df1 = pd.DataFrame({'state_cd': ['CA', 'AZ', 'TX', 'FL', 'NY'],
                    'pop': [100, 25, 65, 55, 70]})

# import data from csv
df=pd.read_csv('P4-Demographic-Data.csv')

# import data from excel 'xlsx'
#for an earlier version of Excel use 'xls'
pip install xlrd
data = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx') 
df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name',...])
# optional - Selecting subset of column/s
data = pd.read_excel (r'C:\Users\Ron\Desktop\Product List.xlsx') 
df = pd.DataFrame(data, columns= ['Product'])


# Export Pandas DataFrame to a CSV File
df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv', index = False, header=True)
df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')




##### Exploring data

# check num of rows and cols in the dataframe
len(df)
df.shape # number of rows and cols
df.ndim # number of dimentions
df.size # number of values (rows x cols)
df.memory_usage() # memory being used by df
df["col1"].value_counts() # number of values in col1

# list columns
df.columns
df.keys()
list(df) # similar to df.columns
len(df.columns) # number of columns

df.head(5) # show top 5 rows
df.tail(=5) # show bottom 5 rows

df.info() # more info about df. similar to str funciton in R
df.describe() # more info about df. similar to summary func in R
df.describe().transpose() # transpose for better readability sometimes

df['DataFrame Column'].count()
df['DataFrame Column'].mean()
df['DataFrame Column'].std() # standard deviation
df['DataFrame Column'].min()
df['DataFrame Column'].quantile(q=0.25) # 25th quartile
df['DataFrame Column'].quantile(q=0.50)
df['DataFrame Column'].quantile(q=0.75)
df['DataFrame Column'].max()

df.agg(('max','min')) # returns rows with max and min age
df.max() # returns row with max age
df.Age.agg(('max')) # returns max age
df.Age.max() # returns max age

# Pandas methods omit nan values when performing calculations unless they are explicitly instructed not to
df.mean(skipna=False)

# sum and count grouped by specific columns
groupby_sum1 = df.groupby(['Country']).sum() 
groupby_count1 = df.groupby(['Country']).count()
df.groupby(['Country']).mean()['Sales'].plot() # can specify a specific column to find mean of. Here we do mean(sales)


# Sum each column:
df.sum(axis=0) 
# Sum each row:
df.sum(axis=1)

# applying numpy / scipy functions
df1 = pd.DataFrame({'A': [1,2,3,4],
                    'B': [2,4,6,8],
                    'C': [10,20,30,40]})
# weighted avg of each row
wt_avg=np.average(df1, axis=1, weights=[10, 5, 1])



##### renaming cols
df.columns=['CountryName', 'CountryCode', 'Birthrate', 
            'Internetusers', 'IncomeGroup'] # removed space between Income Group


##### subsetting dataframes -- subsetting done using [] operator of the dataframe

######## RealPython.com
df['Age'] # returns col Age - pd.Series is returned
df[['Age']] # returns col Age - pd.DataFrame is returned
df.Age # returns col Age - pd.Series is returned

# .loc refers to the label index.
# .iloc refers to the positional index.
# accessor .loc[] is used to get rows or columns by their labels
df.loc[2] # returns row with index=2 - pd.Series is returned
df.iloc[2] # returns row with integer index=2

df.loc[:, 'Age'] # returns column Age - pd.Series is returned
df.iloc[:, 1] # returns column with index 1, which is Age in this case

df.loc[0:3, ['Name', 'Age']] # can specify multiple columns
df.iloc[0:4, [0, 1]] # with .iloc[], the stop index of a slice is exclusive, meaning it is excluded from the returned values

# can skip rows and columns using slicing
df.iloc[0:4:2,[0,1]] # using the slicing construct
df.iloc[slice(0, 4, 2), [0,1]] # using built-in Python class slice()
df.iloc[np.s_[0:4:2], [0,1]] # using numpy.s_[]
df.iloc[pd.IndexSlice[0:4:2], [0,1]] # using pd.IndexSlice[]

# select all rows with a condition
df.loc[df.Age >= 25]
df.loc[(df.Name == 'krish') | (df.Age < 25) ] # multiple conditions
df.loc[cond1 & cond2 | cond3 ^ ~(cond4)] # in case of not ~ the condition needs to be enclosed in brackets
''' # XOR is represented by ^
$x $y ($x or $y) ($x xor $y)
0  0    0          0
1  0    1          1
0  1    1          1
1  1    1          0
'''
df['Age'].loc[df.Age >= 25]
df['Age'].where(cond=df.Age >=25, other=50) # the difference is that where also returns rows where condition is not satisfied but with specified values (NaN is no value is specified)

# access single elements 
df.Name[2] # returns value in col Age row with index 2
# using .at and .iat
df.at[2, 'Name']
df.iat[2, 0]

# setting values
# Change the first name of all rows with an ID greater than 2000 to "John"
data.loc[data['id'] > 2000, "first_name"] = "John"
df.loc[condition_for_rows, ['section', 'city']] = ['S','Pune'] # update specific columns

######## Python A-Z
# subset by rows -- we need to supply row as "numbers"
df[21:26] # 26th not included
df[::-1] # reverse the dataframe
df[::10] # subset with every 10th row from the df

# subset by cols -- we need to supply columns as a list []
df.IncomeGroup.shape # (195,)
df['CountryName'].shape # (195,) 
df[['CountryName']].shape # (195, 1)
df[['CountryName','Internetusers']].shape # (195, 2)

# subset by rows and cols
df[21:26][['CountryName']].shape # (5, 1)
df[['CountryName']][21:26].shape # (5, 1) -- doesnt matter if we specify row or column first

# Select Rows from Pandas DataFrame
df = pd.DataFrame({'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]})
df.loc[2] # returns row 3
# Example 1: Select rows where the price is equal or greater than 10
df.loc[df['Price'] >= 10]
# Example 2: Select rows where the color is green AND the shape is rectangle
df.loc[(df['Color'] == 'Green') & (df['Shape'] == 'Rectangle')]
# Example 3: Select rows where the color is green OR the shape is rectangle
df.loc[(df['Color'] == 'Green') | (df['Shape'] == 'Rectangle')]
# Example 4: Select rows where the price is not equal to 15
df.loc[df['Price'] != 15]





# String operations
s.shelter_city.str.upper() # lower, strip, startswith('char'), endswith, get_dummies, len, 
s.shelter_address.str.split(' ').str[1]
s2=s.shelter_address.str.split(' ', expand=True) # with expand=True, returns a df, else a list
s2.iloc[:,1].str.cat(s2.iloc[:,2], sep=', ')
# col1.str.cat(col2, sep=', ')



##### Basic operations with a dataframe
df=pd.read_csv('P4-Demographic-Data.csv')

# basic math operations on existing cols
res = df.Birthrate * df.Internetusers

# Add a column to df
df['new_col'] = res

# Add a column using df.assign
df = pd.DataFrame({'Product': ['Tablet','iPhone','Laptop','Monitor']})
df=df.assign(price=[100,200,250,150],
            weight=[500,200,1200,2100])

another_col = np.arange(0,195)
df['another_col'] = pd.DataFrame(another_col)

# Add a column using df.insert
df.insert(loc=index_where_column_gets_inserted, 
        column='column-name',
        value=np.array([0,1,2,3,..]))

# Add a new row using df.append(pd.Series)
new_row=pd.Series(data=['iPad',250,750],
                index=df.columns, name=df.shape[0]) # index name = 4
df.append(new_row)

# Drop a row or col 
df.drop('another_col',axis=1) # drop col another_col
df.drop(2, axis=0) # drop row 2


##### Filtering a dataframe
df[df.Internetusers < 2] # rows with internet users < 2
df[df.CountryName=='Malta']


# All countries starting with A
df[df.CountryName.str[0]=='A'] # Getting element wise strings from series and using [0] to get first element 
df[df.CountryName.str.startswith('A')] # Alternate approach, usind built in startswith function
# Series.str.startswith(*args, **kwargs)[source] - Test if the start of each string element matches a pattern.
# Series.str.endswith - Same as startswith, but tests the end of string.
# Series.str.contains - Tests if string element contains a pattern.

# specify multiple conditions using bitwise operator & (not and keyword)
# because bitwise & does the comparison element by element (correct approach) 
# whereas 'and' keyword compares the entire series (df.Internetusers and df.Birthrate) at once (incorrect approach/doesnt make sense)
df[(df.Internetusers < 2)  & (df.Birthrate > 10)] 

# get unique category names
df.IncomeGroup.unique()


##### get values using .at() and .iat()
# .at for labels. Important - even integers are treated as labels
# .iat for integer location. 

df
df.iat[0,0]
df.at[0,'CountryName'] # incidently row label is an integer in this case so we specify without quotes






# Categorical data 
# Features like gender, country, and codes are always repetitive. 
# These are the examples for categorical data.

# benefits
# Converting such a string variable to a categorical variable will save some memory.
# specifying an order on the categories - lexical order of a variable is not the same as the logical order
# signal to other python libraries that this column should be treated as a categorical variable

lst = pandas.Categorical(values, categories, ordered) # returns a list
pd.Series(lst) # convert above to a pandas Series

pd.Categorical(values=['a', 'b', 'c', 'd', 'a', 'b', 'c'])
pd.Categorical(values=['a', 'b', 'c', 'd', 'a', 'b', 'c'], 
        categories=['a', 'b', 'c']) # notice 'd' gets replaced by NaN as we did not specify it in the category list
c=pd.Categorical(values=['a', 'b', 'c', 'd', 'a', 'b', 'c'], 
        categories=['a', 'b', 'c'],
        ordered=True) # specify an order, order = [a < b < c]
c.describe() # get the count and frequency of categories
c.categories # get names of categories
c.ordered # check if ordered or not
c = c.add_categories(['f']) # adds a new category
c = c.remove_categories(['f']) # remove a category

# all comparisons (==, !=, >, >=, <, and <=) of categorical data possible, even to a scalar
cat = pd.Series(pd.Categorical([1,2,3], categories=[1,2,3], ordered=True))
cat1 = pd.Series(pd.Categorical([2,2,2], categories=[1,2,3], ordered=True))
print(cat>cat1)
print(cat>2)





##### Group by
# Any groupby operation involves one (or more) of the following operations on the original object. They are −
# Splitting the Object - ways to split an object like
obj.groupby('key')
obj.groupby(['key1','key2'])
obj.groupby(key,axis=1)

import pandas as pd
import numpy as np
df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]})

df.groupby('Team').groups # View Groups
df.groupby(['Team','Year']).groups # Group by with multiple columns
for name, group in df.groupby('Year'): # Iterating through Groups
   print (name)
   print(group)
df.groupby('Year').get_group(2014) # we can select a single group

# Applying a function
### Aggregation − computing a summary statistic
# aggregated function returns a single aggregated value for each group
df.groupby('Year')['Points'].agg(np.mean) # average
df.groupby('Year')['Points'].agg(np.size) # counts
df.groupby('Year')['Points'].agg([np.sum, np.mean, np.std])
# agg is a df level function, so can be applied directly to a df also
df.groupby('Year')['Points'].sum()

df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
df.apply(np.sqrt) # to entire dataframe
df.apply(np.sum, axis=0)  # to columns
df.apply(np.sum, axis=1) # to rows


### Transformation − perform some group-specific operation
# Transformation on a group or a column returns an object that is indexed the same size of that is being grouped. 
# Thus, the transform should return a result that is the same size as that of a group chunk.
grouped = df.groupby('Team')
# score = lambda x: (x - x.mean()) / x.std()*10
score = lambda x: x + 1 # Applying transform is like applying a function to each element
print(grouped.transform(score))

### Filtration − discarding the data with some condition
# Filtration filters the data on a defined criteria and returns the subset of data. 
# The filter() function is used to filter the data.
df.groupby('Team').filter(lambda x: len(x) >= 3)


# Combining the results

##### Combining Data in Pandas With merge(), .join(), and concat()
'''
merge() for combining data on common columns or indices
.join() for combining data on a key column or an index -- ideally use merge if you are not joining on the index
concat() for combining DataFrames across rows or columns (combine data based on the index) - by default axis=0 (append rows), axis-1 (append columns) can be specified
'''
# merge - When you want to combine data objects based on one or more keys in a similar way to a relational database
# You can achieve both many-to-one and many-to-many joins

merge(left=dataframe, right=dataframe,  # we can merge specific columns: left=dataframe[['col1','col2']], right=dataframe[['col1','col3']],
      left_on=pk_column, right_on=fk_column, # pk-primary key, fk-foreign key
      how='inner', # outer, left, right
      on=join_column, # which columns to join on. used when pk and fk have same column name
      left_index=False, right_index=False, 
      suffixes, # tuple of strings to append to identical column names that are not merge keys
      indicator=True, # adds a column names 'merge' that shows if the data was in 'both' dataframes, 'left_only' or 'right_only'
      ) # can also use ,on=['primary_key','foreign_ky']

# create artificial data using dict
df1 = pd.DataFrame({'state_cd': ['CA', 'AZ', 'TX', 'FL', 'NY'],
                    'pop': [100, 25, 65, 55, 70]})
df2 = pd.DataFrame({'state_code': ['AZ', 'CA', 'FL', 'TX', 'WA'],
                    'pop': [25, 100, 55, 65, 75],
                    'state': ['Arizona', 'California', 'Florida', 'Texas', 'Washington']})

pd.merge(left=df1, right=df2,
      left_on='state_cd', right_on='state_code',
      how='left',
      suffixes=('_df1','_df2')
      )

# Join
df1.join(df2, on=['state_cd','state_code'],
         lsuffix="_df1", rsuffix="_df2")


#### Concat using pd.concat([df1,df2,..]) or df1.append([df2,..])
# for easily combining together Series, DataFrame, and Panel objects.
pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)
'''
objs − This is a sequence or mapping of Series, DataFrame, or Panel objects.
axis − {0, 1, ...}, default 0. This is the axis to concatenate along.
join − {‘inner’, ‘outer’}, default ‘outer’. How to handle indexes on other axis(es). Outer for union and inner for intersection.
ignore_index − boolean, default False. If True, do not use the index values on the concatenation axis. The resulting axis will be labeled 0, ..., n - 1.
join_axes − This is the list of Index objects. Specific indexes to use for the other (n-1) axes instead of performing inner/outer set logic.
'''
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])
two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
pd.concat([one,two],ignore_index=True) # we get a new index range 0 to n-1
pd.concat([one,two],keys=['x','y']) # keys is optional to associate specific keys with each of the pieces of the chopped up DataFrame
pd.concat([one,two],axis=1) # similar to hstack
one.append(two) # similar to pd.concat([one,two])
one.append([two,one,two]) # append function can take multiple objects as well 





# Time Series
# NaT means Not a Time (equivalent to NaN)
pd.datetime.now() # gives you the current date and time
pd.Timestamp('2017-03-01') # convert a date into a timestamp
pd.Timestamp(1587687255,unit='s') # convert integer or float epoch times to timestamp
pd.date_range("11:00", "13:30", freq="30min").time # Create a Range of Time
pd.date_range("11:00", "13:30", freq="H").time # Change the Frequency of Time
pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])) # convert a Series or list-like object of date-like objects
pd.to_datetime(['2005/11/23', '2010.12.31', None])

pd.date_range('1/1/2011', periods=5) # Create a Range of Dates
pd.date_range('1/1/2011', periods=5,freq='M') # Change the Date Frequency
pd.date_range('1/1/2011', periods=5) # Unlike date_range(), it excludes Saturday and Sunday.
# default frequency for date_range is a calendar day while the default for bdate_range is a business day
'''Ofset aliases
S - secondly freq
T,min - minutely freq
H - hourly
B - business day freq
D - calendar day frequency     
W - weekly
M - month end freq
MS - month start frequency
Q - quarter end
QS - quarter start
A - annual year end
'''
# Timedeltas are differences in times, expressed in difference units, for example, days, hours, minutes, seconds. 
# They can be both positive and negative.
pd.Timedelta('2 days 2 hours 15 minutes 30 seconds') # 2 days 02:15:30
pd.Timedelta(6,unit='h') # 0 days 06:00:00
pd.Timedelta(days=2) #  2 days 00:00:00

pd.to_timedelta(1587687255,unit='s') # convert seconds to days
# date operations using timedelta
pd.datetime.now() + pd.Timedelta(days=1) # add 1 day to current date
pd.datetime.now() - pd.Timedelta(days=1) # remove 1 day to current date

# Resampling and Rolling
# Resampling
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
        9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
        21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24,
        freq='H')
temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)

# If you want to split a day into four six-hour intervals and get the mean temperature for each interval
temp.resample(rule='6h').mean()
# Each row corresponds to a single six-hour interval
# temp_c value is the mean of the six temperatures from the datetime specified in the row
# .min(), .max(), .sum() can also be used

# Rolling
temp.rolling(window=3).mean() # rolling mean based on current row and previous 2 row values






# Convert Index to Column
df.reset_index(inplace=True) # convert index to column
df = df.rename(columns = {'index':'new column name'}) # rename the “index” header to a customized header

# Alternatively
df.set_index("column_name", inplace=True)




# Set a single column as Index
df.set_index('column')
# Set multiple columns as MultiIndex
df.set_index(['column_1','column_2',...])




# Check for NaN in Pandas DataFrame
# Check for NaN under a single DataFrame column:
df['your column name'].isnull().values.any()
# Count the NaN under a single DataFrame column:
df['your column name'].isnull().sum()
# Check for NaN under an entire DataFrame:
df.isnull().values.any()
# Count the NaN under an entire DataFrame:
df.isnull().sum().sum()


# select all rows with NaN under a single DataFrame column
df[df['column name'].isna()]
# select all rows with NaN under a single DataFrame column
df[df['column name'].isnull()]
# select all rows with NaN under an entire DataFrame
df[df.isna().any(axis=1)]
# select all rows with NaN under an entire DataFrame
df[df.isnull().any(axis=1)]

# Filling Missing Data
# can also use the optional parameter inplace=True with .fillna()
df_.fillna(value=0, inpace=True) # Specified values
df_.fillna(method='ffill') # The values above the missing value
df_.fillna(method='bfill') # The values below the missing value
df_.interpolate() # replace missing values with interpolated values

# Replace values in Pandas DataFrame
# Replace a single value with a new value for an individual DataFrame column
df['column name'] = df['column name'].replace(['old value'],'new value')
# Replace multiple values with a new value for an individual DataFrame column
df['column name'] = df['column name'].replace(['1st old value','2nd old value',...],'new value')
# Replace multiple values with multiple new values for an individual DataFrame column
df['column name'] = df['column name'].replace(['1st old value','2nd old value',...],['1st new value','2nd new value',...])
# Replace a single value with a new value for an entire DataFrame
df = df.replace(['old value'],'new value')




# Replace character/s under a single DataFrame column
df['column name'] = df['column name'].str.replace('old character','new character')
# Replace character/s under the entire DataFrame
df = df.replace('old character','new character', regex=True)




# filter Pandas DataFrame based on the index
df = df.filter(like = 'index to keep', axis=0)




# Find Where Python is Installed on Windows
import sys
locate_python = sys.exec_prefix
print(locate_python)



# Sort an Index in Pandas DataFrame
# In an ascending order
df = df.sort_index()
# In a descending order
df = df.sort_index(ascending=False)



# Sort Pandas DataFrame
df = pd.DataFrame({'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]})
# A column in an ascending order
df.sort_values(by=['Brand'], inplace=True)
# A column in a descending order
df.sort_values(by=['Brand'], inplace=True, ascending=False)
# By multiple columns – Case 1
 df.sort_values(by=['Year','Price'], inplace=True)


# Drop Rows by Index in Pandas DataFrame
# Drop a single row by index. For example, you may use the syntax below to drop the row that has an index of 2
df = df.drop(index=2)
# Drop multiple rows by index. For instance, to drop the rows with the index values of 2, 4 and 6, use
df = df.drop(index=[2,4,6])




# Drop Columns from Pandas DataFrame
# Drop a single column from the DataFrame
df = df.drop('column name',axis=1)
# Drop multiple columns from the DataFrame
df = df.drop(['column 1','column 2','column 3',...],axis=1)



# Randomly Select Rows from Pandas DataFrame
# Randomly select a single row
df = df.sample()
# Randomly select a specified number of rows. For example, to select 3 random rows, set n=3
df = df.sample(n=3)
# Allow a random selection of the same row more than once (by setting replace=True)
df = df.sample(n=3,replace=True)
# Randomly select a specified fraction of the total number of rows. For example, if you have 8 rows, and you set frac=0.50, then you’ll get a random selection of 50% of the total rows, meaning that 4 rows will be selected
df = df.sample(frac=0.50)




# Randomly Select Columns from Pandas DataFrame
# Randomly select a single column
df = df.sample(axis='columns')
# Randomly select a specified number of columns. For example, to select 3 random columns, set n=3
df = df.sample(n=3,axis='columns')
# Allow a random selection of the same column more than once (by setting replace=True)
df = df.sample(n=3,axis='columns',replace=True)
# Randomly select a specified fraction of the total number of columns (for example, if you have 6 columns, and you set frac=0.50, then you’ll get a random selection of 50% of the total columns, meaning that 3 columns will be randomly selected)
df = df.sample(frac=0.50,axis='columns')



# Change Strings to Uppercase/lowercase in Pandas DataFrame
df['column name'].str.upper() # lower()




# Add Prefix/Suffix to Each Column Name in Pandas DataFrame
df = df.add_suffix('your suffix')
df = df.add_prefix('my_prefix')



# scenarios to get all rows that:
# Contain a specific substring
contain_values = df[df['Month'].str.contains('Ju')]
# Contain one substring OR another substring
contain_values = df[df['Month'].str.contains('Ju|Ma')]
# Do NOT contain given substrings
contain_values = df[~df['Month'].str.contains('Ju|Ma')]
# Contain a specific numeric value
contain_values = df[df['Days in Month'].astype(str).str.contains('0')]






# Convert Integers to Datetime in Pandas DataFrame
df['DataFrame Column'] = pd.to_datetime(df['DataFrame Column'], 
                        format=specify your format)

dt=pd.DataFrame({'Dates':[20190902, 20190913, 20190921],
                  'ShortDates':[190902, 190913, 190921],
                  'dttm':[20190902093000, 20190913093000, 20190921200000],
                  'Status':['Opened', 'Opened', 'Closed']})

dt['FormattedDates'] = pd.to_datetime(dt['Dates'], format='%Y%m%d')
dt['FormattedShortDates'] = pd.to_datetime(dt['ShortDates'], format='%y%m%d')
dt['FormattedDateTimes'] = pd.to_datetime(dt['dttm'], format='%Y%m%d%H%M%S')



# Convert a column to numeric
data = {'set_of_numbers': [1,2,"AAA",3,"BBB",4]}
df = pd.DataFrame(data,columns=['set_of_numbers'])
df['set_of_numbers'] = pd.to_numeric(df['set_of_numbers'], errors='coerce')
# np.nan is used to signify Not a Number values


# Convert String to Floats
# astype(float) method
df['DataFrame Column'] = df['DataFrame Column'].astype(float)
# to_numeric method
df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'],errors='coerce')



# Convert Integers to Floats in Pandas DataFrame
# The astype(float) method
df['DataFrame Column'] = df['DataFrame Column'].astype(float)
# The to_numeric method
df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'], downcast='float')


# Convert Integers to Strings in Pandas DataFrame
# map(str)
df['DataFrame Column'] = df['DataFrame Column'].map(str)
# apply(str)
df['DataFrame Column'] = df['DataFrame Column'].apply(str)
# astype(str)
df['DataFrame Column'] = df['DataFrame Column'].astype(str)
# values.astype(str)
df['DataFrame Column'] = df['DataFrame Column'].values.astype(str)



# Convert String to Integer
# The astype(int) method:
df['DataFrame Column'] = df['DataFrame Column'].astype(int)
# The to_numeric method:
df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'])



# How to Create a Time Delay in Python
import time
time.sleep(number of seconds of delay)
# 3 seconds time delay
import time
time.sleep(3)
# 3 minutes time delay
import time
time.sleep(3 * 60)





# Check the Data Type in Pandas DataFrame
df.dtypes
df['DataFrame Column'].dtypes



# Drop Rows with NaN Values
df.dropna()
# After dropping rows you can Reset the Index
df.reset_index(drop=True)





# Compare Values in two Pandas DataFrames
# number of rows in the two dataframes should match
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Product1': ['Computer','Phone','Printer','Desk'],
                   'Price1': [1200,800,200,350]
                   })
df2 = pd.DataFrame({'Product2': ['Computer','Phone','Printer','Desk'],
                    'Price2': [900,800,300,350]
                    })
# add a column  showing if the price between two dataset matches 
df1['pricesMatch?'] = np.where(df1['Price1'] == df2['Price2'], 'True', 'False') 
                  # np.where(condition,'value if true','value if false')
# add a column showing the price difference
df1['priceDiff?'] = np.where(df1['Price1'] == df2['Price2'], 0, df1['Price1'] - df2['Price2'])



# Pivoting dataframe
# Count Duplicates in Pandas DataFrame
# df.pivot_table(index=['DataFrame Column'], aggfunc='size')
df = pd.DataFrame({'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'values': ['700','ABC300','700','900XYZ','800','700','800','550']
        })
# duplicate under a single column
df.pivot_table(index=['Color'], aggfunc='size')
# duplicate across multiple columns
df.pivot_table(index=['Color','Shape'], aggfunc='size')
# duplicate when having NaN values in the DataFrame
df['values'] = pd.to_numeric(df['values'], errors='coerce')
df.pivot_table(index=['values'], aggfunc='size')
### we can also fill NaN with NULL and then it will appear in the pivot output
df['values'] = df['values'].fillna('NULL')
df.pivot_table(index=['values'], aggfunc='size')

# Another example
df = pd.DataFrame({'Name of Employee': ['Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill'],
             'Sales': [1000,300,400,500,800,1000,500,700,50,60,1000,900,750,200,300,1000,900,250,750,50],
             'Quarter': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
             'Country': ['US','Japan','Brazil','UK','US','Brazil','Japan','Brazil','US','US','US','Japan','Brazil','UK','Brazil','Japan','Japan','Brazil','UK','US']
            })
# Let’s say that your goal is to determine the:
# Total sales per employee
df.pivot_table(index=['Name of Employee'], values=['Sales'], aggfunc='sum')
# Total sales by country
df.pivot_table(index=['Country'], values=['Sales'], aggfunc='sum')
# Sales by both employee and country
df.pivot_table(index=['Name of Employee','Country'], values=['Sales'], aggfunc='sum')
# Max individual sale by country
df.pivot_table(index=['Country'], values=['Sales'], aggfunc='max')
# Mean, median and min sales by country
df.pivot_table(index=['Country'], values=['Sales'], aggfunc={'median','mean','min'})
df.pivot_table(index=['Country'], values=['Sales'], aggfunc={'median','mean','min'}).plot()

# Groupby has some of similar funcitonality
df.groupby(['Country']).mean()['Sales'].plot() # can specify a specific column to find mean of. Here we do mean(sales)






### we can also replace NaA with other values instead of NULL
# For a single column using Pandas: 
df['DataFrame Column'] = df['DataFrame Column'].fillna(0)
# For a single column using NumPy:
df['DataFrame Column'] = df['DataFrame Column'].replace(np.nan, 0)
# For an entire DataFrame using Pandas:
df.fillna(0)
# For an entire DataFrame using NumPy:
df.replace(np.nan,0)

# If condition to replace null values with 0
df.loc[df['col_name'].isnull(), 'col_name'] = 0



# Round Values in Pandas DataFrame
# Round to specific decimal places – Single DataFrame column
df['DataFrame column'].round(decimals=number of decimal places needed)
# Round up – Single DataFrame column
df['DataFrame column'].apply(np.ceil)
# Round down – Single DataFrame column
df['DataFrame column'].apply(np.floor)
# Round to specific decimals places – Entire DataFrame
df.round(decimals=number of decimal places needed)




# apply LEFT, RIGHT, MID in Pandas
df = pd.DataFrame({'Identifier': ['AB-55555-111$ PQ','CD-77777-222$ RS','EF-99999-333$ TU']})
# From the left
df['Identifier'].str[:2]
# From the right
df['Identifier'].str[-2:]
# From the middle
df['Identifier'].str[3:8]
# Before a symbol
df['Identifier'].str.split('-').str[0]
# Before space
df['Identifier'].str.split(' ').str[0]
# After a symbol
df['Identifier'].str.split('-').str[2]
# Between identical symbols
df['Identifier'].str.split('-').str[1]
# Between different symbols
temp=df['Identifier'].str.split('-').str[2]
temp.str.split('$').str[0]



# Concatenate Column Values in Pandas DataFrame
# This gives an err: ‘TypeError: ufunc 'add' did not contain a loop with signature matching types
df1 = df['1st Column Name'] + df['2nd Column Name'] + ...
# Correct way
df1 = df['1st Column Name'].map(str) + df['2nd Column Name'].map(str) + ...

df1 = pd.DataFrame({'Day': [1,2,3,4,5], 
        'Month': ['Jun','Jul','Aug','Sep','Oct'], 
        'Year': [2016,2017,2018,2019,2020]} )
df2 = pd.DataFrame({'Unemployment Rate': [5.5,5,5.2,5.1,4.9], 
         'Interest Rate': [1.75,1.5,1.25,1.5,2]} )
# Example 1: Concatenating values using a single DataFrame
df['date'] = df1['Day'].map(str) + '-' + df1['Month'].map(str) + '-' + df1['Year'].map(str)
# Example 2: Concatenating two DataFrames
df_combined = df1['Day'].map(str) + '-' + df1['Month'].map(str) + '-' + df1['Year'].map(str) + ': ' + 'Unemployment: ' + df2['Unemployment Rate'].map(str) + '; ' + 'Interest: ' + df2['Interest Rate'].map(str)
# Example 3: Concatenating two DataFrames, and then finding the maximum value
df1 = pd.DataFrame({'Set1': [55,22,11,77,33]} ) 
df2 = pd.DataFrame({'Set2': [23,45,21,73,48]} )
Concatenated = df1['Set1'].map(str) + df2['Set2'].map(str)
df_combined = pd.DataFrame(Concatenated, columns=['Combined Values'])
max1 = df_combined['Combined Values'].max()





#  IF condition - syntax and common use cases
df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'

# Set of numbers
df = pd.DataFrame({'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]})
# If the number is <= 4, then True else False
df.loc[df['set_of_numbers'] <= 4, 'equal_or_lower_than_4?'] = 'True' 
df.loc[df['set_of_numbers'] > 4, 'equal_or_lower_than_4?'] = 'False' 
# do the same in one statement using lambda
df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(
        lambda x: 'True' if x <= 4 else 'False')

# Strings
df = pd.DataFrame({'First_name': ['Jon','Bill','Maria','Emma']})
# If name='Bill' then 'Match', else 'Mismatch'
df.loc[df['First_name'] == 'Bill', 'name_match'] = 'Match'  
df.loc[df['First_name'] != 'Bill', 'name_match'] = 'Mismatch'  
# do the same in one statement using lambda
df['name_match'] = df['First_name'].apply(
        lambda x: 'Match' if x == 'Bill' else 'Mismatch')

# AND/OR conditions
# If the name is 'Bill' or 'Emma', then 'Match'
df.loc[(df['First_name'] == 'Bill') | (df['First_name'] == 'Emma'), 'name_match'] = 'Match'  
# if the name is neither 'Bill' nor 'Emma', then 'Mismatch'
df.loc[(df['First_name'] != 'Bill') & (df['First_name'] != 'Emma'), 'name_match'] = 'Mismatch'  

# If condition to replace null values with 0
df.loc[df['col_name'].isnull(), 'col_name'] = 0



# Iterating Over a Pandas DataFrame
# Pandas provides several more convenient methods for iteration:
# .items() to iterate over columns
# .iteritems() to iterate over columns
for col_label, col in df.iteritems():
        print(col_label, col, sep='\n', end='\n\n')
# .iterrows() to iterate over rows
for row_label, row in df.iterrows():
        print(row_label, row, sep='\n', end='\n\n')
# .itertuples() to iterate over rows and get named tuples
for row in df.loc[:, ['name', 'city', 'total']].itertuples():
        print(row)

