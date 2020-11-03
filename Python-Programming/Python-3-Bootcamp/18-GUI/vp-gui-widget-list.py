# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:40:53 2020

@author: vivek
"""

# a list of the GUI widgets available

# For a complete list of the GUI widgets available to you, you can list the registered widget types. Widget is the base class
import ipywidgets as widgets

# Show all available widgets!
for item in widgets.Widget.widget_types.items():
    print(item[0][2][:-5])
    
# Numeric widgets
# IntSlider
widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

# FloatSlider
widgets.FloatSlider(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

# Sliders can also be displayed vertically.
widgets.FloatSlider(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='vertical',
    readout=True,
    readout_format='.1f',
)

# IntRangeSlider
widgets.IntRangeSlider(
    value=[5, 7],
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
)

# FloatRangeSlider
widgets.FloatRangeSlider(
    value=[5, 7.5],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

# IntProgress
widgets.IntProgress(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Loading:',
    bar_style='', # 'success', 'info', 'warning', 'danger' or ''
    orientation='horizontal'
)

# FloatProgress
widgets.FloatProgress(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Loading:',
    bar_style='info',
    orientation='horizontal'
)

# BoundedIntText
widgets.BoundedIntText(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Text:',
    disabled=False
)

# BoundedFloatText
widgets.BoundedFloatText(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Text:',
    disabled=False
)

# IntText
widgets.IntText(
    value=7,
    description='Any:',
    disabled=False
)

# FloatText
widgets.FloatText(
    value=7.5,
    description='Any:',
    disabled=False
)

# Boolean widgets
ToggleButton
widgets.ToggleButton(
    value=False,
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='check'
)

# Checkbox
widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)

# Valid
widgets.Valid(
    value=False,
    description='Valid!',
)

# Selection widgets
# Dropdown
widgets.Dropdown(
    options=['1', '2', '3'],
    value='2',
    description='Number:',
    disabled=False,
)

widgets.Dropdown(
    options={'One': 1, 'Two': 2, 'Three': 3},
    value=2,
    description='Number:',
)

# RadioButtons
widgets.RadioButtons(
    options=['pepperoni', 'pineapple', 'anchovies'],
    # value='pineapple',
    description='Pizza topping:',
    disabled=False
)

# Select
widgets.Select(
    options=['Linux', 'Windows', 'OSX'],
    value='OSX',
    # rows=10,
    description='OS:',
    disabled=False
)

# SelectionSlider
widgets.SelectionSlider(
    options=['scrambled', 'sunny side up', 'poached', 'over easy'],
    value='sunny side up',
    description='I like my eggs ...',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True
)

# SelectionRangeSlider

import datetime
dates = [datetime.date(2015,i,1) for i in range(1,13)]
options = [(i.strftime('%b'), i) for i in dates]
widgets.SelectionRangeSlider(
    options=options,
    index=(0,11),
    description='Months (2015)',
    disabled=False
)

# ToggleButtons
widgets.ToggleButtons(
    options=['Slow', 'Regular', 'Fast'],
    description='Speed:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Description of slow', 'Description of regular', 'Description of fast'],
    # icons=['check'] * 3
)

# SelectMultiple
widgets.SelectMultiple(
    options=['Apples', 'Oranges', 'Pears'],
    value=['Oranges'],
    # rows=10,
    description='Fruits',
    disabled=False
)

# String widgets
# Text
widgets.Text(
    value='Hello World',
    placeholder='Type something',
    description='String:',
    disabled=False
)

# Textarea

widgets.Textarea(
    value='Hello World',
    placeholder='Type something',
    description='String:',
    disabled=False
)


# Label widget is useful if you need to build a custom description next to a control using similar styling to the built-in control description

widgets.HBox([widgets.Label(value="The $m$ in $E=mc^2$:"), widgets.FloatSlider()])

# HTML
widgets.HTML(
    value="Hello <b>World</b>",
    placeholder='Some HTML',
    description='Some HTML',
)

# HTML Math

widgets.HTMLMath(
    value=r"Some math and <i>HTML</i>: \(x^2\) and $$\frac{x+1}{x-1}$$",
    placeholder='Some HTML',
    description='Some HTML',
)

# Image
file = open("images/WidgetArch.png", "rb")
image = file.read()
widgets.Image(
    value=image,
    format='png',
    width=300,
    height=400,
)

# Button
widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'
)



#########################################3


# Advanced Widget List
import ipywidgets as widgets

# Output widget can capture and display stdout, stderr and rich output generated by IPython. 
# After the widget is created, direct output to it using a context manager.
out = widgets.Output()
out

# You can print text to the output area as shown below.
with out:
    for i in range(10):
        print(i, 'Hello world!')
        
# Rich material can also be directed to the output area
from IPython.display import YouTubeVideo
with out:
    display(YouTubeVideo('eWzY2nGfkXk'))
    
# Play (Animation) widget
# The Play widget is useful to perform animations by iterating on a sequence of integers with a certain speed. 
play = widgets.Play(
    # interval=10,
    value=50,
    min=0,
    max=100,
    step=1,
    description="Press play",
    disabled=False
)
slider = widgets.IntSlider()
widgets.jslink((play, 'value'), (slider, 'value'))
widgets.HBox([play, slider])

# Date picker
widgets.DatePicker(
    description='Pick a Date',
    disabled=False
)

# Color picker
widgets.ColorPicker(
    concise=False,
    description='Pick a color',
    value='blue',
    disabled=False
)

# Controller
# The Controller allows a game controller to be used as an input device.
widgets.Controller(
    index=0,
)

# Container/Layout widgets
# These widgets are used to hold other widgets, called children. Each has a children property that may be set either when the widget is created or later.
# Box
items = [widgets.Label(str(i)) for i in range(4)]
widgets.Box(items)

# HBox
items = [widgets.Label(str(i)) for i in range(4)]
widgets.HBox(items)

# VBox
items = [widgets.Label(str(i)) for i in range(4)]
left_box = widgets.VBox([items[0], items[1]])
right_box = widgets.VBox([items[2], items[3]])
widgets.HBox([left_box, right_box])

# Accordion
accordion = widgets.Accordion(children=[widgets.IntSlider(), widgets.Text()])
accordion.set_title(0, 'Slider')
accordion.set_title(1, 'Text')
accordion

# Tabs
# In this example the children are set after the tab is created. Titles for the tabes are set in the same way they are for Accordion.
tab_contents = ['P0', 'P1', 'P2', 'P3', 'P4']
children = [widgets.Text(description=name) for name in tab_contents]
tab = widgets.Tab()
tab.children = children
for i in range(len(children)):
    tab.set_title(i, str(i))
tab


# Accordion and Tab use selected_index, not value
# Unlike the rest of the widgets discussed earlier, the container widgets Accordion and Tab update their selected_index attribute when the user changes which accordion or tab is selected
# That means that you can both see what the user is doing and programmatically set what the user sees by setting the value of selected_index

selected_index = None # closes all of the accordions or deselects all tabs
# In the cells below try displaying or setting the selected_index of the tab and/or accordion.
tab.selected_index = 3
accordion.selected_index = None

# Nesting tabs and accordions¶
# Tabs and accordions can be nested as deeply as you want. If you have a few minutes, try nesting a few accordions or putting an accordion inside a tab or a tab inside an accordion.
# The example below makes a couple of tabs with an accordion children in one of them
tab_nest = widgets.Tab()
tab_nest.children = [accordion, accordion]
tab_nest.set_title(0, 'An accordion')
tab_nest.set_title(1, 'Copy of the accordion')
tab_nest















