
# tidypython




################# dfply ##################

# https://github.com/kieferk/dfply#the-x-dataframe-symbol

# pip installation
pip install dfply
# conda installation
conda install -c tallic dfply

from dfply import * 

women = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-08/women.csv')
df = women

# chaining operations on the data with the >> operator, or alternatively 
# starting with >>= for inplace operations.
# Columns can be specified either by their name (string) or an integer
lowprice = diamonds >> head(10) >> tail(3)

diamonds >> select(X.carat, X.cut) >> head(3)
diamonds >> select(1, X.price, ['x', 'y']) >> head(2)
diamonds >> drop(1, X.price, ['x', 'y']) >> head(2)
diamonds >> select(~X.carat, ~X.color, ~X.clarity) >> head(2) # not operator, returns same as above drop statement

# select filters
diamonds >> select(starts_with('c')) >> head(2)
diamonds >> drop(columns_from(X.price)) >> head(2)
# mixing techniques to select first 2 cols, 'category' col and last 2 cols
diamonds >> select(columns_to(1, inclusive=True), 'depth', columns_from(-2)) >> head(2)
'''
    starts_with(prefix): find columns that start with a string prefix.
    ends_with(suffix): find columns that end with a string suffix.
    contains(substr): find columns that contain a substring in their name.
    everything(): all columns.
    columns_between(start_col, end_col, inclusive=True): find columns between a specified start and end column. The inclusive boolean keyword argument indicates whether the end column should be included or not.
    columns_to(end_col, inclusive=True): get columns up to a specified end column. The inclusive argument indicates whether the ending column should be included or not.
    columns_from(start_col): get the columns starting at a specified column.
'''
# Subsetting and filtering
diamonds >> row_slice([10,15]) # diamonds.iloc[[10,15]]
diamonds >> row_slice(list(range(5,10))) # diamonds.iloc[10:15]
diamonds >> group_by('cut') >> row_slice(5)

diamonds >> sample(frac=0.0001, replace=False) # % of df rows returned
diamonds >> sample(n=3, replace=True) # number of rows returned

diamonds >> distinct(X.color) # Selection of unique rows
diamonds >> mask(X.cut == 'Ideal') >> head(4) # Filtering rows with logical criteria 
# mask() can also be called using the alias filter_by()
diamonds >> filter_by(X.cut == 'Ideal', X.color == 'E', X.table < 55, X.price < 500) 

# pull simply retrieves a column and returns it as a pandas series, in case you only care about one particular column at the end of your pipeline
(diamonds
 >> filter_by(X.cut == 'Ideal', X.color == 'E', X.table < 55, X.price < 500)
 >> pull('carat'))

# DataFrame transformation
diamonds >> mutate(x_plus_y=X.x + X.y) >> select(columns_from('x')) >> head(3)
diamonds >> mutate(x_plus_y=X.x + X.y, y_div_z=(X.y / X.z)) >> select(columns_from('x')) >> head(3)
# The transmute() function is a combination of a mutate and a selection of the created variables.
diamonds >> transmute(x_plus_y=X.x + X.y, y_div_z=(X.y / X.z)) >> head(3)

# group_by() and ungroup()
diamonds >> head(5) >> group_by(X.color) >> mutate(avg_price=X.price.mean())

(diamonds >> group_by(X.cut) >>
 mutate(price_lead=lead(X.price), price_lag=lag(X.price)) >>
 head(2) >> select(X.cut, X.price, X.price_lead, X.price_lag))
# ungroup()
(diamonds >> group_by(X.cut) >> arrange(X.price) >>
 head(3) >> ungroup() >> mask(X.carat < 0.23))

# Reshaping
diamonds >> arrange(X.table, ascending=False) >> head(5)
diamonds >> rename(CUT=X.cut, COLOR='color') >> head(2)

# transform a "wide" DataFrame into a "long" format
# gather(key, value, *columns, add_id=True) melts the specified columns into two key:value columns
diamonds >> gather('variable', 'value', ['price', 'depth','x','y','z']) >> head(5)
elongated = diamonds >> gather('variable', 'value', add_id=True) 

# transform a "long" DataFrame into a "wide" format
# In this case the _ID column comes in handy since it is necessary to not have any duplicated identifiers.
widened = elongated >> spread(X.variable, X.value)
widened.dtypes # all are objects
# convert dtypes when spreading
widened = elongated >> spread(X.variable, X.value, convert=True)
widened.dtypes # dtype based on the data in each column

# separate(column, into, sep="[\W_]+", remove=True, convert=False, extra='drop', fill='right')
# Columns can be split into multiple columns
# default sep is -
# positional sep can be specified using [2,4]. Meaning the second and fourth item in string are separators
'''
    column: the column to split.
    into: the names of the new columns.
    sep: either a regex string or integer positions to split the column on.
    remove: boolean indicating whether to remove the original column.
    convert: boolean indicating whether the new columns should be converted to the appropriate type (same as in spread above).
    extra: either drop, where split pieces beyond the specified new columns are dropped, or merge, where the final split piece contains the remainder of the original column.
    fill: either right, where np.nan values are filled in the right-most columns for missing pieces, or left where np.nan values are filled in the left-most columns.
'''
d=pd.DataFrame({'a':['1-a-3', '1-b', '1-c-3-4', '9-d-1', '10']})
d >> separate(X.a, ['col1', 'col2', 'col3','col4'], sep='-', remove=True, convert=True,
              extra='drop', fill='right') # extra='merge'
d >> separate(X.a, ['col1', 'col2', 'col3','col4'], sep=[2,4], remove=True, convert=True,
              extra='drop', fill='right') # extra='merge'

# unite(colname, *args, sep='_', remove=True, na_action='maintain')
'''
    colname: the name of the new joined column.
    *args: list of columns to be joined, which can be strings, symbolic, or integer positions.
    sep: the string separator to join the columns with.
    remove: boolean indicating whether or not to remove the original columns.
    na_action: can be one of "maintain" (the default), "ignore", or "as_string". The default "maintain" will make the new column row a NaN value if any of the original column cells at that row contained NaN. "ignore" will treat any NaN value as an empty string during joining. "as_string" will convert any NaN value to the string "nan" prior to joining.
'''
d=pd.DataFrame({'a':[1,2,3],
                'b':['a','b','c'],
                'c':[True, False, np.NaN]})
d >> unite('united', X.a, 'b', 2, remove=False, na_action='maintain')
d >> unite('united', ['a','b','c'], remove=True, na_action='ignore', sep='*')
d >> unite('united', d.columns, remove=True, na_action='as_string')


# Joining
a = pd.DataFrame({'x1':['A','B','C'],
                'x2':[1,2,3]})
b = pd.DataFrame({'x1':['A','B','D'],
                'x3':[True,False,True]})
a >> inner_join(b, by='x1')
'''
    inner_join(other, by='column')
    outer_join(other, by='column') (which works the same as full_join())
    right_join(other, by='column')
    left_join(other, by='column')
    semi_join(other, by='column')
    anti_join(other, by='column')
'''

# Set operations filter a DataFrame based on row comparisons with another DataFrame.
'''
    other: the DataFrame to compare to
    index: a boolean (default False) indicating whether to consider the pandas index during comparison.
    keep: string (default "first") to be passed through to .drop_duplicates() controlling how to handle duplicate rows.
'''
a >> union(c) # returns rows that appear in either DataFrame
a >> intersect(c) # returns rows that appear in both DataFrames
a >> set_diff(c) # returns the rows in the left DataFrame that do not appear in the right DataFrame

# Binding - convenience wrappers around pandas.concat() for joining DataFrames by rows or by columns
# bind_rows() - joining two DataFrames "vertically".
# bind_rows(other, join='outer', ignore_index=False)
# pandas.concat([df, other], join=join, ignore_index=ignore_index, axis=0)
a >> bind_rows(b, join='inner')
a >> bind_rows(b, join='outer')

# bind_cols() - joining DataFrames "horizontally"
# bind_cols(other, join='outer', ignore_index=False)
# pandas.concat([df, other], join=join, ignore_index=ignore_index, axis=1)
a >> bind_cols(b)


# Summarization
# summarize(**kwargs) takes an arbitrary number of keyword arguments that will 
# return new columns labeled with the keys that are summary functions of columns 
# in the original DataFrame.
diamonds >> summarize(price_mean=X.price.mean(), price_std=X.price.std())
diamonds >> group_by('cut') >> summarize(price_mean=X.price.mean(), price_std=X.price.std())

# summarize_each(function_list, *columns) is a more general summarization function. 
# It takes a list of summary functions to apply as its first argument and then a 
# list of columns to apply the summary functions to. Columns can be specified with 
# either symbolic, string label, or integer position like in the selection functions 
# for convenience.
diamonds >> summarize_each([np.mean, np.var], X.price, 'depth')
diamonds >> group_by(X.cut) >> summarize_each([np.mean, np.var], X.price, 4)

# Summary functions
# mean(series)
diamonds >> groupby(X.cut) >> summarize(price_mean=mean(X.price))
# first(series, order_by=None)
diamonds >> groupby(X.cut) >> summarize(price_first=first(X.price))
# last(series, order_by=None)
diamonds >> groupby(X.cut) >> summarize(price_last=last(X.price))
# nth(series, n, order_by=None)
diamonds >> groupby(X.cut) >> summarize(price_penultimate=nth(X.price, -2))
# n(series)
diamonds >> groupby(X.cut) >> summarize(price_n=n(X.price))
# n_distinct(series)
diamonds >> groupby(X.cut) >> summarize(price_ndistinct=n_distinct(X.price))
# IQR(series)
diamonds >> groupby(X.cut) >> summarize(price_iqr=IQR(X.price))
# colmin(series)
diamonds >> groupby(X.cut) >> summarize(price_min=colmin(X.price))
# colmax(series)
diamonds >> groupby(X.cut) >> summarize(price_max=colmax(X.price))
# median(series)
diamonds >> groupby(X.cut) >> summarize(price_median=median(X.price))
# var(series)
diamonds >> groupby(X.cut) >> summarize(price_var=var(X.price))
# sd(series)
diamonds >> groupby(X.cut) >> summarize(price_sd=sd(X.price))


# Embedded column functions
# Window functions - perform operations on vectors of values that return a vector of the same length
# lead() and lag()
# The lead(series, n) function pushes values in a vector upward, adding NaN values 
# in the end positions. Likewise, the lag(series, n) function pushes values downward, 
# inserting NaN values in the initial positions. Both are calls to pandas 
# Series.shift() function under the hood.
(diamonds >> mutate(price_lead=lead(X.price, 2), price_lag=lag(X.price, 2)) >>
            select(X.price, -2, -1) >>
            head(6))
# between(series, a, b, inclusive=False) function checks to see if values are between two given bookend values.
diamonds >> select(X.price) >> mutate(price_btwn=between(X.price, 330, 340)) >> head(6)
# dense_rank(series, ascending=True) function is a wrapper around the scipy function for calculating dense rank.
diamonds >> select(X.price) >> mutate(price_drank=dense_rank(X.price)) >> head(6)
# min_rank(series, ascending=True) is a wrapper around the scipy ranking function with min rank specified.
diamonds >> select(X.price) >> mutate(price_mrank=min_rank(X.price)) >> head(6)
# cumsum(series) function calculates a cumulative sum of a column.
diamonds >> select(X.price) >> mutate(price_cumsum=cumsum(X.price)) >> head(6)
# cummean(series)
diamonds >> select(X.price) >> mutate(price_cummean=cummean(X.price)) >> head(6)
# cummax(series)
diamonds >> select(X.price) >> mutate(price_cummax=cummax(X.price)) >> head(6)
# cummin(series)
diamonds >> select(X.price) >> mutate(price_cummin=cummin(X.price)) >> head(6)
# cumprod(series)
diamonds >> select(X.price) >> mutate(price_cumprod=cumprod(X.price)) >> head(6)


# Extending dfply with custom functions
# https://github.com/kieferk/dfply/blob/master/examples/basics-extending-functionality.ipynb


############### dplython #################

from dplython import (DplyFrame, X, diamonds, select, sift,
  sample_n, sample_frac, head, arrange, mutate, group_by,
  summarize, DelayFunction)
df = DplyFrame(df)

df >> head(5)
df >> sample_n(5)
df >> select(X.name, X.category, X.country, X.role, X.description)
df >> sift(X.category == 'Leadership') # As in pandas, use bitwise logical operators like |, & (, is same as &)
df >> arrange(X.country) # couldnt find a way to sort descending so moved to dfply library
df >> mutate(carat_bin=X.carat.round())
df >> group_by(X.category) >> summarize(num_of_people = X.name.count())

# It's possible to pass the entire dataframe using X._
# The special Later name, "_" will refer to the entire DataFrame. 

# Combine multiple
(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.category)
    >> summarize(num_of_people = X.name.count())
).set_index('category').plot(title='# of Women Recognized by Category', y='num_of_people', ylabel='', legend=False, kind='pie')

