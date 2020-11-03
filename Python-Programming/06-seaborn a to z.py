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



