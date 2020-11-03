# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:33:26 2020

@author: vivek
"""

# http://www.pygal.org/en/stable/documentation/index.html

import pygal
pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render()

import pygal                                                       # First import pygal
bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file

bar_chart = pygal.Bar()
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.render()

