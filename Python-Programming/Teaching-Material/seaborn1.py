#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:12:32 2017

@author: vivekparashar
"""
%matplotlib inline

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

#Plotting univariate distributions
np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size=100)

sns.distplot(x); #by default bins are chosen automatically and histogram and kde are plotted      

sns.distplot(x, bins=20, hist=True, kde=True, rug=False);

sns.rugplot(x); #can be drawn separately
sns.kdeplot(x, shade=True); #can be drawn separately
           


#Plotting bivariate distributions           
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

iris = sns.load_dataset("iris")
sns.jointplot(x="x", y="y", data=df);           

sa=iris.reset_index().values
sns.jointplot(x=sa.sepal_length, y=sa.petal_width, data=df);           
sa[:,0]

x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k");


iris = sns.load_dataset("iris")
sns.pairplot(iris);
            
            