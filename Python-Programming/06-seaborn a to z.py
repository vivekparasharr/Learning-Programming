# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:29:50 2020

@author: vivek
"""

# adjust location of legend on a plot
legend='best'

# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=8,4 # make the chart wider


# use seaborn datasets
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.info


# import data
df=pd.read_csv('P4-Demographic-Data.csv')

v1 = sns.distplot(df['Internet users'], bins=20)

v2 = sns.boxplot(data=df, x='Income Group', y='Birth rate')

# linear model plot
v3 = sns.lmplot(data=df, x='Internet users', y='Birth rate', fit_reg=False, 
                hue='Income Group', size=5, aspect=2) # aspect - 0 (square), 0.5 (vertical rectange), 2 (horizontal rectangle) 
# seems like an inverse relationship



# Facet grid
import matplotlib.pyplot as plt 
import seaborn as sns 
df=df[:20] # making the dataset smaller so its faster to render
g=sns.FacetGrid(df, row='round_stage', col='location', hue='obstacle_name')
kws=dict(s=50, linewidth=0.5, edgecolor='black') # passing these values through dictionary is optional
g=g.map(plt.scatter, 'season', 'obstacle_order', **kws)

# optional
# adjust the x and y axis limits
g.set(xlim=(start, end), ylim=(start, end))
# put a diagonal on each chart
for ax in g.axes.flat:
    ax.plot((0,100), (0,100), c="gray", ls="--")
# add ledend
g.add_legend()

# seaborn dashboard
# for seaborn native plots we need to specify the ax=axes[x,y]
sns.set_style('darkgrid') # white, whitegrid, dark, darkgrid, ticks
f, axes = plt.subplots(2,2,figsize=(15,15))
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0])
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])
z=sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating', ax=axes[1,0])
# for matplotlib plots such as hist, we can specify axis as axes[x,y].hist(...)
# axes[1,1].hist(movies.CriticRating, bins=15) 
k4 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, \
    shade=True, shade_lowest=False, cmap='Reds', \
    ax=axes[1,1])
plt.show()

# styling tips
# chart background - change cgart background to black
sns.set_stype('dark', {"axes.facecolor":"black"}) # white, whitegrid, dark, darkgrid, ticks
f, axes = plt.subplots(2,2,figsize=(15,15))
# plot [0,0]
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, \
    shade=True, shade_lowest=True, cmap='inferno', \
    ax=axes[0,0])
k1b=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, \
    cmap='cool', ax=axes[0,0])
# plot [0,1]
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, \
    shade=True, shade_lowest=True, cmap='inferno', ax=axes[0,1])
k2b=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, \
    cmap='cool', ax=axes[0,1])
# plot [1,0]
# palette is used to specify color for violin plot
# YlOrRd - Yellow Orange Red
z=sns.violinplot(data=movies, x='Year', y='CriticRating', \
    palette='YlOrRd', ax=axes[1,0])
# plot [1,1]
# for matplotlib plots such as hist, we can specify axis as axes[x,y].hist(...)
# axes[1,1].hist(movies.CriticRating, bins=15) 
# _r in cmap is to reverse color map
k4 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, \
    shade=True, shade_lowest=False, cmap='Blues_r', \
    ax=axes[1,1])
k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating, \
    cmap='gist_gray_r', ax=axes[1,1])
# show all plots
plt.show()

# make stacked histogram chart
list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
h=plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()

# style this chart
list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
# change the size of charts by always creating a chart in a fig
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27) # A4 sheet size in inches

h=plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels, color=[pass-list-of-colors-based-on-number-of-categories])
plt.title('Movie Budget Distribution', fontsize=35, color='DarkBlue', fontname='Console',)
plt.ylabel('...', color='Green')
plt.yticks(fontsize=20) 
plt.legend(frameon=True, fancybox=True, shadow=True, \
    framealpha=1, prop={'size':20}) # prop used to change text size of legend
# framealpha for transparency
plt.show()

