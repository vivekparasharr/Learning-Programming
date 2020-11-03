
# arrays
# python has inbuilt arrays and well as numpy arrays
# we just use numpy array as the inbuilt ones are less flexible
l=[546,375,254,651,781,569,454,564]

import numpy as np
a=np.array(l)
# if we convert a list with multiple data types (such as int, string, boolean, etc.)
# the numpy.array() function will convery all elements into a string, so it becomes an array of strings
# so data type of all elements in an array are same

print(a)

# when you slice an array you dont create a copy of an array
# so any modification to the slice of an array will be reflected in the actual array
a=[1,2,3,4]
a=np.array(a) # array([1, 2, 3, 4])
b=a[0:2]
b[:]=111 # array([1, 2])
# now, b becomes array([111, 111])
# but c also becomes array([111, 111,   3,   4])

# lets say we have an array a
a=[1,2,3,4]
np.where(a == np.max(a))
# numpy.where() function iterates over a bool array, and for every True, it yields corresponding the element array x, and for every False, it yields corresponding item from array y. So, it returns an array of elements from x where the condition is True and elements from y elsewhere. 
# in our example we get (array([x,y,z,..], dtype=int64),) as output
# this means, max value of the array exists at following indices array([x,y,z,..],)
# if max value exists in muliple places then all indices where it exists will be returned

# building your first matrix
import numpy as np
a=np.arange(0,20)
np.reshape(a,(5,4),order='F') # order is optional, if not specified then 'C' is the default order
# we could also do
a.reshape(5,4)
# C (default behavior) - matrix gets filled row by row, similar to C
# F - matrix gets filled column by column, similar to Fortran

# INDEXING
# MULTI DIMENTIONAL LIST  -  CONVERT INTO A NUMPY ARRAY AND THEN INDEXING
L= [ [1,2,3], [4,5,6] , [7,8,9] ] # this list has 3 rows and 3 columns
L=np.array(L)
L[1,1] # returns 5
L[0,:] # returns first row; we could also just say L[0]
L[:,0] # returns first column

# Dictionary is quite useful in matrix indexing, example
m=np.array([[1,2,3],[4,5,6],[7,8,9]])
col_names={'age':0,'weight':1,'height':2}
row_names={'vivek':0,'ale':1,'neety':2}
# now we can get weight of ale using actual indexes or dict indexes
m[1,1] # 5
m[row_names['ale'],col_names['weight']] # 5

# arithmetic operation is element by element 
# division by zero shows a warning, and the result of div by zero is nan
# result can be rounded using matrix.round method
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
A+B
A-B
A*B
np.matrix.round(A/B)
A**B

# visualization
import numpy as np
import matplotlib.pyplot as plt
# in jupyter notebook we need to specify %matplotlib inline
plt.rcParams['figure.figsize']=8,4 # just need to set it once, can alter the size of plots

plt.plot(m[0], c='Blue',ls='--',marker='s',ms=17,label='vivek') # c is color, ls - line style, marker='s' - square marker, marker size=17
plt.plot(m[1], c='Magenta',ls='--',marker='s',ms=17,label='ale')
plt.plot(m[2], c='Green',ls='--',marker='s',ms=17,label='neety')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.xticks([0,1,2],['age','weight','height'],rotation='vertical') #xticks replaces 0,1,2 in x-axis with 'age','weight','height'. We could also specify [0,1,2] using range function like list(range(0,3))
plt.show()



# Covariance matrix
data = np.array([[45,37,42,35,39],
                [38,31,26,28,33],
                [10,15,17,21,12]])
covMatrix = np.cov(data,bias=True)
sns.heatmap(covMatrix, annot=True, fmt='g')

# Create a Correlation Matrix using Pandas
df = pd.DataFrame({'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]})
corrMatrix=df.corr()
sns.heatmap(corrMatrix, annot=True)

