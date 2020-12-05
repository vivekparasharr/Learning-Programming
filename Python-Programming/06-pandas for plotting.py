
import pandas as pd
import matplotlib.pyplot as plt

'''
.plot() has several optional parameters. Most notably, the kind parameter accepts eleven different string values and determines which kind of plot you’ll create:
The default value is "line"
"area" is for area plots.
"bar" is for vertical bar charts.
"barh" is for horizontal bar charts.
"box" is for box plots.
"hexbin" is for hexbin plots.
"hist" is for histograms.
"kde" is for kernel density estimate charts.
"density" is an alias for "kde".
"line" is for line graphs. (DEFAULT)
"pie" is for pie charts.
"scatter" is for scatter plots.
''' 

# Scatter diagram
df = pd.DataFrame({'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       })
df.plot(x ='Unemployment_Rate', y='Stock_Index_Price', kind = 'scatter')   

# Line chart
df = pd.DataFrame({'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       })
df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')

# Line chart - pivot and plot
df = pd.DataFrame({'Name of Employee': ['Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill'],
             'Sales': [1000,300,400,500,800,1000,500,700,50,60,1000,900,750,200,300,1000,900,250,750,50],
             'Quarter': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
             'Country': ['US','Japan','Brazil','UK','US','Brazil','Japan','Brazil','US','US','US','Japan','Brazil','UK','Brazil','Japan','Japan','Brazil','UK','US']
            })
df.pivot_table(index=['Country'], values=['Sales'], aggfunc={'median','mean','min'}).plot()

# Line chart - groupby and plot
df.groupby(['Country']).mean()['Sales'].plot()


# Bar chart
df = pd.DataFrame({'Country': ['USA','Canada','Germany','UK','France'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
       })
df.plot(x ='Country', y='GDP_Per_Capita', kind = 'bar')

# Pie chart
df = pd.DataFrame({'Tasks': [300,500,700]})
df.plot.pie(y='Tasks',figsize=(5, 5),autopct='%1.1f%%', startangle=90)



# RealPython.com
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')

# %matplotlib - Using matplotlib backend: MacOSX
# %matplotlib inline - Jupyter Notebook

# Line chart - a line graph containing data from every row in the DataFrame
# Using matplotlib
plt.plot(df["Rank"], df["P75th"])
# Using pandas
df.plot(x="Rank", y="P75th")

# Line chart with multiple series
df.plot(x="Rank", y=["P25th", "Median", "P75th"])

'''
.plot() has several optional parameters. Most notably, the kind parameter accepts eleven different string values and determines which kind of plot you’ll create:
The default value is "line"
"area" is for area plots.
"bar" is for vertical bar charts.
"barh" is for horizontal bar charts.
"box" is for box plots.
"hexbin" is for hexbin plots.
"hist" is for histograms.
"kde" is for kernel density estimate charts.
"density" is an alias for "kde".
"line" is for line graphs. (DEFAULT)
"pie" is for pie charts.
"scatter" is for scatter plots.
'''

# Histogram
# Lets see the distribution of data and if there are any outliers
df["Median"].plot(kind="hist")

# Bar plots
# Vertical and horizontal bar charts are often a good choice if you want to see the difference between your categories
# Plotting outliers
top_5 = df.sort_values(by="Median", ascending=False).head()
top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)

# Let’s investigate all majors whose median salary is above $60,000
top_medians = df[df["Median"] > 60000].sort_values("Median")
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")

# Scatter plot
# see whether two columns of a dataset are connected
df.plot(x="Median", y="Unemployment_rate", kind="scatter")


# Analyze Categorical Data - groupby
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
# Bar chart - horizontal
cat_totals.plot(kind="barh", fontsize=4)

# Determining Ratios
# If you’re interested in ratios, then pie plots are an excellent tool
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]
# # Adding a new item "Other" with the sum of the small categories
small_sums = pd.Series([small_cat_totals.sum()], index=["Other"]) 
big_cat_totals = big_cat_totals.append(small_sums)
big_cat_totals.plot(kind="pie", label="")


# Zooming in on Categories
# Histogram - plot showing the distribution of the median earnings for the engineering majors
df[df["Major_category"] == "Engineering"]["Median"].plot(kind="hist")


# More syntax
# DataFrame plotting accessor and method
DataFrame.plot([x, y, kind, ax, ….])
# Draw a stacked area plot.
DataFrame.plot.area([x, y])
# Vertical bar plot.
DataFrame.plot.bar([x, y])
# Make a horizontal bar plot.
DataFrame.plot.barh([x, y])
# Make a box plot of the DataFrame columns.
DataFrame.plot.box([by])
# Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.density([bw_method, ind])
# Generate a hexagonal binning plot.
DataFrame.plot.hexbin(x, y[, C, …])
# Draw one histogram of the DataFrame’s columns.
DataFrame.plot.hist([by, bins])
# Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.kde([bw_method, ind])
# Plot Series or DataFrame as lines.
DataFrame.plot.line([x, y])
# Generate a pie plot.
DataFrame.plot.pie(**kwargs)
# Create a scatter plot with varying marker point size and color.
DataFrame.plot.scatter(x, y[, s, c])
# Make a box plot from DataFrame columns.
DataFrame.boxplot([column, by, ax, …])
# Make a histogram of the DataFrame’s.
DataFrame.hist([column, by, grid, …])




