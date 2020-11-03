# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:40:20 2020

@author: vivek
"""

# https://altair-viz.github.io/gallery/index.html
# https://vega.github.io/vega-lite/tutorials/getting_started.html
# the charts can be seen in a  jupyter notebook

import altair as alt

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()


# Basic Statistical Visualization
import pandas as pd
source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]})
# mark_point() is for scatter plot
chart = alt.Chart(source).mark_bar().encode(
    x='a',
    y='average(b)', # switch x,y to make hbar chart
)
chart.save('chart.html')

alt.Chart(data).mark_rect().encode(
    x='a',
    y='b', 
    color='c'
)


from vega_datasets import data
data.barley().columns

alt.Chart(data.barley()).mark_bar().encode(
    x='variety',
    y='sum(yield)',
    color='site'
)

import altair as alt
import numpy as np
import pandas as pd

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)


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

