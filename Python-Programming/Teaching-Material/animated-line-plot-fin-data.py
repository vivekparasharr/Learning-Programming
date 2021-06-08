
# Let’s make a map! Using Geopandas, Pandas and Matplotlib to make a Choropleth map
# https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT
import os

df=pd.read_csv('/Users/vivekparashar/Downloads/fin-data.csv')

df=df[df.stk_pr.notna()]
df.plot(x='stk_pr', y='cov_cl_pr', kind='line')

df.cov_cl_pr

output_path='/Users/vivekparashar/Downloads/fin_data'

for i in range(1,23):
    y=10+i
    df2 = df.iloc[:i]
    fig=df2.plot(x='stk_pr', y='cov_cl_pr', xlim=(84,108),ylim=(-6,11), kind='line')
    filepath = os.path.join(output_path, str(y)+'_charts.png')
    fig.get_figure().savefig(filepath, dpi=80)

df=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-10/mobile.csv')

