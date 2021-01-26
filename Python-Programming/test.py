
a=10
b=2
c=a+b
print(c)

import seaborn as sns
import matplotlib.pyplot as plt 

ax = sns.lmplot()

import altair as alt
from vega_datasets import data

counties = alt.topo_feature(data.us_10m.url, 'counties')
source = data.unemployment.url

alt.Chart(counties).mark_geoshape().encode(
    color='rate:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(source, 'id', ['rate'])
).project(
    type='albersUsa'
).properties(
    width=500,
    height=300
)

import seaborn as sns
tips = sns.load_dataset('tips')

tips.mean() # shows mean of all numeric variables
tips.median() # shows median of all numeric variables
tips.mode() # shows mode of all variables
tips.total_bill.var() # variance of total_bill variable
tips.total_bill.std() # standard deviation of total_bill variable
range = tips.total_bill.max() - tips.total_bill.min() # range
tips.total_bill.quantile(.75) - tips.total_bill.quantile(.25) # IQR
# coefficient of variance
cv = lambda x: x.std() / x.mean() * 100
cv(tips.total_bill)

import scipy.stats as s
s.skew(tips.total_bill, bias=False)  #calculate sample skewness
s.kurtosis(tips.total_bill, bias=False)  #calculate sample kurtosis

