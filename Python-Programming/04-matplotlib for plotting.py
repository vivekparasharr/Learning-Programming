
import math
import numpy as np 
from matplotlib import pyplot as plt 
# from pylab import *
# PyLab is a convenience module that bulk imports matplotlib.pyplot (for plotting) and NumPy (for Mathematics and working with arrays) in a single name space. Although many examples use PyLab, it is no longer recommended.

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,color='green', marker='o', linestyle='-.',linewidth=2, markersize=12) 
# plt.plot(x,y,'ob') - only observations will be showsn, not the line
plt.show()

'''
linestyle - -- -. : 
marker . , o v ^ < 1 2 3 4 s p * h H + x D d | _
color b g r c m y k w
'''

# sine, cos, square and other funcitons
x = np.linspace(-3, 3, 30)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), 'r-')
plt.plot(x, -np.sin(x), 'g--')

x = np.linspace(-3, 3, 30)
plt.plot(x, x**2, 'b.-')


# bar chart
x = [5,8,10] 
y = [12,16,6]  
x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 

# stacked bar chart
x = [1,2,3] 
y = [12,16,6]  
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x, y2, bottom=y, color = 'g', align = 'center') 

# histogram
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
# hist,bins = np.histogram(a,bins = [0,20,40,60,80,100]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 

# pie chart
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
plt.pie(students, labels = langs,autopct='%1.2f%%')

# scatter plot
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(grades_range, girls_grades, color='r')
plt.scatter(grades_range, boys_grades, color='b')

# box plot
# summary of a set of data containing the minimum, first quartile, median, third quartile, and maximum
# draw a box from the first quartile to the third quartile
# A vertical line goes through the box at the median
# The whiskers go from each quartile to the minimum or maximum
data_to_plot = np.random.normal(100, 10, 200)
plt.boxplot(data_to_plot)

# violin plot
# similar to box plots, except that they also show the probability density of the data at different values
data_to_plot = np.random.normal(100, 10, 200)
plt.violinplot(data_to_plot)

# 3d plotting
# from mpl_toolkits import mplot3d

# 3d plot
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
plt.axes(projection='3d').plot3D(x, y, z, 'gray')

# 3d scatter plot
plt.axes(projection='3d').scatter(x, y, z, c='green')

# 3D Contour Plot
def f(x, y):
   return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.axes(projection='3d').contour3D(X, Y, Z, 50, cmap='binary')

# 3d wireframe plot - parameters similar to contoour plot
plt.axes(projection='3d').plot_wireframe(X, Y, Z, color='black')
# 3d surface plot - parameters similar to contoour plot
plt.axes(projection='3d').plot_surface(X, Y, Z,cmap='viridis', edgecolor='none')





# Matplotlib - Object-oriented Interface
# x=np.linspace(-3, 3, 30)
x = np.arange(0, math.pi*2, 0.05)
y=np.sin(x)
# Figure class is a top-level container for all plot elements. The Figure object is instantiated by calling the figure() function from the pyplot module
# fig = plt.figure(figsize=(width,height), dpi, facecolor, edgecolor, linewidth)
fig = plt.figure() # create a figure instance which provides an empty canvas
# Axis object - A given figure can contain many Axes, but a given Axes object can only be in one Figure
# The Axes contains two (or three in the case of 3D) Axis objects
# Axes object is added to figure by calling the add_axes() method
ax=fig.add_axes([0,0,1,1])  # add axes to figure using add_axes([left, bottom, width, height of the figure])
ax.set_title("sine wave") # Set labels for x and y axis as well as title
ax.set_xlabel('angle')
ax.set_ylabel('sine')
# legend() method of axes class adds a legend to the plot figure. It takes three parameters
# ax.legend(handles, labels= ('aa','bb',..), loc='lower right') 
# loc can be 0 (best), 1 (upper right), 2 (upper left), 3 (LL), 4 (LR), 5 (R), 6 (center left), 7 (cr), 8 (lower center), 9 (upper center), 10 (center) 
ax.plot(x,y) # Invoke the plot() method of the axes object
plt.show()



# Matplotlib - Multiplots
# subplot() function allows you to plot different things in the same figure
x = np.arange(1,11) 
y = 2 * x + 5 
####
plt.subplot(2, 1, 1)
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,color='green', marker='o', linestyle='-.',linewidth=2, markersize=12) 
####
plt.subplot(2, 1, 2)
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,color='blue', marker='o', linestyle='-.',linewidth=2, markersize=12) 
####
plt.show()

# inset plot - add_subplot() function of the figure class will not overwrite the existing plot −
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(221, facecolor='y')
ax2.plot([1,2,3])

# You can add an insert plot in the same figure by adding another axes object in the same figure canvas.
x = np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y = np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()

# subplots() which acts as a utility wrapper and helps in creating common layouts of subplots, including the enclosing figure object, in a single call.
# The two integer arguments to this function specify the number of rows and columns of the subplot grid
fig,a =  plt.subplots(2,2)
import numpy as np
x = np.arange(1,5)
a[0][0].plot(x,x*x)
a[0][0].set_title('square')
a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')
a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')
plt.show()


# Subplot2grid() gives more flexibility in creating an axes object at a specific location of the grid
# It also allows the axes object to be spanned across multiple rows or columns
a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)
import numpy as np
x = np.arange(1,10)
a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()


# grid() function of axes object sets visibility of grid inside the figure to on or off
# you can also display major / minor (or both) ticks of the gris
# Additionally color, linestyle and linewidth properties can be set in the grid() function
fig, axes = plt.subplots(1,3, figsize = (12,4))
x = np.arange(1,11)
axes[0].plot(x, x**3, 'g',lw=2)
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='b', ls = '-.', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()
plt.show()



# Formatting Axes to use Logarithmic scale
fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)
axes[0].plot( x, np.exp(x))
axes[0].plot(x,x**2)
axes[0].set_title("Normal scale")
axes[1].plot (x, np.exp(x))
axes[1].plot(x, x**2)
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()


# Axis spines are the lines connecting axis tick marks demarcating boundaries of plot area
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])
plt.show()


# Setting Limits - it is possible to set the limits explicitly by using set_xlim() and set_ylim() functions
fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])
x = np.arange(1,10)
a1.plot(x, np.exp(x),'r')
a1.set_title('exp')
a1.set_ylim(0,10000)
a1.set_xlim(0,10)
plt.show()



# Setting Ticks and Tick Labels
x = np.arange(0, math.pi*2, 0.05)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
y = np.sin(x)
ax.plot(x, y)
ax.set_xlabel('angle')
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([-1,0,1])
plt.show()


# Twin Axes - have dual x or y axes in a figure
fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])
x = np.arange(1,11)
a1.plot(x,np.exp(x))
a1.set_ylabel('exp')
a2 = a1.twinx()
a2.plot(x, np.log(x),'ro-')
a2.set_ylabel('log')
fig.legend(labels = ('exp','log'),loc='upper left')
plt.show()




