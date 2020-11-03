# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:58:22 2020

@author: vivek
"""

### statsmodels vs sklearn
# both packages are frequently tagged with python, statistics, and data-analysis
# differences between them highlight what each in particular has to offer: 
# scikit-learn’s other popular topics are machine-learning and data-science; 
# StatsModels are econometrics, generalized-linear-models, timeseries-analysis, and regression-models



### Introduction

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Example 1
# Load data
dat = sm.datasets.get_rdataset("Guerry", "HistData").data
# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()
# Inspect the results
print(results.summary())


# Example 2
# Generate artificial data (2 regressors + constant)
X = np.random.random((100, 2))
X = sm.add_constant(X)
beta = [1, .1, .5]
e = np.random.random(100)
y = np.dot(X, beta) + e

# Fit regression model
results = sm.OLS(y, X).fit()

# Inspect the results
print(results.summary())








### Getting started

# very simple case-study is designed to get you up-and-running quickly with statsmodels
import statsmodels.api as sm
import pandas
from patsy import dmatrices # patsy is a Python library for describing statistical models and building Design Matrices using R-like formulas

# import Guerry dataset, a collection of historical data used in support of Andre-Michel Guerry’s 1833 Essay on the Moral Statistics of France
df = sm.datasets.get_rdataset("Guerry", "HistData").data

# sel specific columns from the dataset
vars = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = df[vars]

df = df.dropna() # eliminate missing values (represented by NaN in a dataframe)

df[-5:] # returns last 5 rows of data

# We want to know whether literacy rates in the 86 French departments are 
# associated with per capita wagers on the Royal Lottery in the 1820s

# methodology
# We need to control for the level of wealth in each department
# we also want to include a series of dummy variables on the right-hand side of our regression equation to control for unobserved heterogeneity due to regional effects

# model is estimated using ordinary least squares regression (OLS)

# To fit most of the models covered by statsmodels, you will need to create two design matrices
# endog - is a matrix of endogenous variable(s) (i.e. dependent, response, regressand, etc.)
# exog - is a matrix of exogenous variable(s) (i.e. independent, predictor, regressor, etc.)
y, X = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')

# dmatrices has
# split the categorical Region variable into a set of indicator variables.
# added a constant to the exogenous regressors matrix.
# returned pandas DataFrames instead of simple numpy arrays. 
# patsy determined that elements of Region were text strings, so it treated Region as a categorical variable. patsy’s default is also to include an intercept, so we automatically dropped one of the Region categories.

# Fitting a model in statsmodels typically involves 3 easy steps
mod = sm.OLS(y, X) # Use the model class to describe the model
res = mod.fit() # Fit the model using a class method
print(res.summary()) # Inspect the results using a summary method

# res object has many useful attributes
res.params
res.rsquared
dir(res) # for a full list of attributes.


# Diagnostics and specification tests
# Rainbow test for linearity (the null hypothesis is that the relationship is properly modelled as linear):
sm.stats.linear_rainbow(res) # returns (test statistic based on the F test, pvalue of the test)
print(sm.stats.linear_rainbow.__doc__) # use this to interpret the output

# we can draw a plot of partial regression for a set of regressors by
sm.graphics.plot_partregress('Lottery', 'Wealth', ['Region', 'Literacy'],
                             data=df, obs_labels=False)

# Alternatively we can use seaborn
import seaborn as sns
sns.lmplot(data=df, y="Lottery", x="Wealth",z_score=0)#, hue="Region")


### statsmodels is using endog and exog as names for the data, the observed variables that are used in an estimation problem. A mnemonic hint to keep the two terms apart is that exogenous has an “x”, as in x-variable, in its name. 
# endogenous: caused by factors within the system
# exogenous: caused by factors outside the system







### API Import for interactive use
import statsmodels.api as sm
dir(sm)
dir(sm.graphics)
dir(sm.tsa)




##############################################################################
# https://www.statsmodels.org/stable/user-guide.html
# https://online.stat.psu.edu/statprogram/
##############################################################################




### Linear Regression
# Linear models with independently and identically distributed errors, 
# and for errors with heteroscedasticity or autocorrelation

# this module allows estimation by 
# ordinary least squares (OLS), 
# weighted least squares (WLS), 
# generalized least squares (GLS), and 
# feasible generalized least squares with autocorrelated AR(p) errors.

# Load modules and data
import numpy as np 
import statsmodels.api as sm
spector_data = sm.datasets.spector.load(as_pandas=False)
spector_data.exog = sm.add_constant(spector_data.exog, prepend=False)
# Fit and summarize OLS model
mod = sm.OLS(spector_data.endog, spector_data.exog) 
res = mod.fit()
print(res.summary())

# OLS is a special case of WLS where all weights are 1
# Ordinary Least Squares
# Artificial data:
c1=np.ones(100) # a column of 100 1s
c2 = np.linspace(0, 10, 100) # a col of 100 evenly spaced numbers between 10-100
c3 = c2**2 # a col with elements which are square of elements in c1
X = np.column_stack((c1, c2, c3)) # stack 1-D arrays as columns to get a single 2-D array

beta = np.array([1, 0.1, 10]) # beta is the coefficient estimated by regression
e = np.random.normal(size=100) # e is the intercept estimated by regression

y = np.dot(X, beta) + e # simple linear regression equation


# Fit and summary:
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

# Quantities of interest can be extracted directly from the fitted model. 
# Type dir(results) for a full list
print('Parameters: ', results.params)
print('R2: ', results.rsquared)


# aspects of the data (such as nonconstant variance or outliers) 
# require a different method for estimating the regression line
# ordinary least squares assumes that there is constant variance in the errors (which is called homoscedasticity). 
# The method of weighted least squares can be used when the ordinary least squares assumption of constant variance in the errors is violated (which is called heteroscedasticity)

import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.api as sm

cols=['parent','progeny','sd']
dta=np.array([
            [0.21, 0.1726, 0.01988],
            [0.2, 0.1707, 0.01938],
            [0.19, 0.1637, 0.01896],
            [0.18, 0.164, 0.02037],
            [0.17, 0.1613, 0.01654],
            [0.16, 0.1617, 0.01594],
            [0.15, 0.1598, 0.01763]
            ])
df = pd.DataFrame(data=dta, columns=cols)

sns.lmplot(data=df, x='parent', y='progeny', ci=None)

model = sm.OLS(np.array(df['progeny']), np.array(df['parent']))
results = model.fit()
print(results.summary())
results.params





# Weighted Least Squares - useful when exog (IV) are homoscedastic
# Artificial data: Heteroscedasticity 2 groups
# Model assumptions:
# Misspecification: true model is quadratic, estimate only linear
# Independent noise/error term
# Two groups for error variance, low and high variance groups
np.random.seed(1024)
c1 = np.ones(50)
c2 = np.linspace(0, 20, 50) # 50 values between 0-20
c3 = (c2 - 5)**2
X = np.column_stack((c1, c2, c3 ))

beta = [5., 0.5, -0.01]
e = np.random.normal(size=50)

y = np.dot(X, beta) + 0.5 * c1 * e
X = X[:,[0,1]]

sns.relplot(data=np.column_stack((X,y)))


mod_wls = sm.WLS(y, X, weights=1./(c1 ** 2))
res_wls = mod_wls.fit()
print(res_wls.summary())


