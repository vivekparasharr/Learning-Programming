
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


########################################################################
####################### visualization tutorial #########################
########################################################################

import seaborn as sns
tips = sns.load_dataset("tips") # tips dataset can be loaded from seaborn
sns.get_dataset_names() # to get a list of other available datasets

import plotly.express as px
tips = px.data.tips() # tips dataset can be loaded from plotly
# data_canada = px.data.gapminder().query("country == 'Canada'")

import pandas as pd
tips.to_csv('/Users/vivekparashar/Downloads/tips.csv')

import altair as alt

import statsmodels.api as sm

# Dot plot shows changes between two (or more) points in time or between two (or more) conditions.
t = tips.groupby(['day','sex']).mean()[['total_bill']].reset_index()
px.scatter(t, x='day', y='total_bill', color='sex', 
        title='Average bill by gender by day', 
        labels={'day':'Day of the week', 'total_bill':'Average Bill in $'})

# Bar (vertical and horizontal)
tips.groupby('sex').mean()['total_bill'].plot(kind='bar') # using pandas plot
tips.groupby('sex').mean()['tip'].plot(kind='barh')

t = tips.groupby(['day','sex']).mean()[['total_bill']].reset_index()
px.bar(t, x='day', y='total_bill') # Using plotly
px.bar(t, x='total_bill', y="day", orientation='h')

# Stacked Bar - need to unstack one of the levels and fill na values
tips.groupby(['day','sex']).mean()[['total_bill']]\
        .unstack('sex').fillna(0)\
        .plot(kind='bar', stacked=True) # using pandas plot; kind='barh' for horizontal plot 

t = tips.groupby(['day','sex']).mean()[['total_bill']].reset_index()
px.bar(t, x="day", y="total_bill", color="sex", title="Average bill by Gender and Day") # vertical 
px.bar(t, x="total_bill", y="day", color="sex", title="Average bill by Gender and Day", orientation='h') # horizontal

# Boxplot (vertical and horizontal)
# we specify y=variable for vertical and x=variable for horizontal for horizontal box plot respectively
tips[['total_bill']].plot(kind='box') # using pandas plot
px.box(tips, y='total_bill') # using plotly
sns.boxplot(y=tips["total_bill"]) # using seaborn

# options for the boxplot in statsmodels include violin_plot and bean_plot
# Violin plot
sns.violinplot(y=tips.total_bill)
sns.violinplot(data=tips, x='day', y='total_bill', 
        hue='smoker', 
        palette='muted', split=True,
        scale='count', inner='quartile',
        order=['Thur','Fri','Sat','Sun'])

sns.catplot(x='sex', y='total_bill',
        hue='smoker', col='time',
        data=tips, kind='violin', split=True,
        height=4, aspect=.7)


# Histogram
tips.total_bill.plot(kind='hist') # using pandas plot
px.histogram(tips, x="total_bill") # using plotly
sns.histplot(data=tips, x="total_bill") # using seaborn
alt.Chart(tips).mark_bar().encode(alt.X('total_bill:Q', bin=True),y='count()') # using altair

# Probability Plot is a way of visually comparing the data coming from different distributions.
# Can be of two types - pp plot or qq plot
# pp plot - (Probability-to-Probability) plot is the way to visualize the comparing of cumulative distribution function (CDFs) of the two distributions (empirical and theoretical) against each other.
# qq plot - (Quantile-to-Quantile) plot is used to compare the quantiles of two distributions. The quantiles can be defined as continuous intervals with equal probabilities or dividing the samples between a similar way The distributions may be theoretical or sample distributions from a process, etc. 
# Normal probability plot is a case of the qq plot. It is a way of knowing whether the dataset is normally distributed or not
import statsmodels.graphics.gofplots as sm 
import numpy as np
sm.ProbPlot(np.array(tips.total_bill)).ppplot(line='s') # using statsmodels
sm.ProbPlot(np.array(tips.total_bill)).qqplot(line='s') # using statsmodels

# Scatter
px.scatter(tips, x='total_bill', y='tip', color='sex', size='size', hover_data=['day']) # using plotly
tips.plot(x='total_bill', y='tip', kind='scatter') # using pandas plot

# Needle


# Reg
sns.regplot(x="total_bill", y="tip", data=tips, marker='+') # using seaborn
sns.regplot(x="size", y="total_bill", data=tips, x_jitter=.1) # for categorical variables we can add jitter to see overlapping points

# Line
tips['total_bill'].plot(kind='line') # using pandas plot

px.line(tips, y='total_bill', title='Total bill') # using plotly

t = tips.groupby('day').sum()[['total_bill']].reset_index()
px.line(t, x='day',y='total_bill', title='Total bill by day')

alt.Chart(t).mark_line().encode(x='day', y='total_bill') # using altair

sns.lineplot(data=t, x='day', y='total_bill') # using seaborn

# Area
tips.groupby('day').sum()[['total_bill']].plot(kind='area') # using pandas plot

t = tips.groupby(['day','sex']).count()[['total_bill']].reset_index()
t_pivoted = t.pivot(index='day', columns='sex', values='total_bill')
t_pivoted.plot.area() # stacked area can be done using pandas.plot as well

px.area(t, x='day', y='total_bill', color='sex',line_group='sex') # using plotly

alt.Chart(t).mark_area().encode(x='day', y='total_bill') # using altair

# Pie
tips.groupby('sex').count()['tip'].plot(kind='pie') # using pandas plot

px.pie(df, values='tip', names='day') # using plotly

# Sunburst - visualize hierarchical data spanning outwards radially from root to leaves
px.sunburst(tips, path=['sex', 'day', 'time'], values='total_bill', color='day')

# Radar
t = tips.groupby('day').mean()[['total_bill']].reset_index()
px.line_polar(t, r='total_bill', theta='day', line_close=True) # using plotly


