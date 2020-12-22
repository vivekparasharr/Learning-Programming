# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:29:50 2020

@author: vivek
"""

# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=8,4 # make the chart wider

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
# for matplotlib plots such as hist, we can specify axis as axes[x,y].hist(...)
sns.set_style('darkgrid')
f, axes = plt.subplots(2,2,figsize=(15,15))
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0])
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])
z=sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating', ax=axes[1,0])
axes[1,1].hist(movies.CriticRating, bins=15) 
plt.show()

# styling tips



