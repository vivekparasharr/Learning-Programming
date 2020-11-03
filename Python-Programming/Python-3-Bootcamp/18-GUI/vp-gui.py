# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:46:46 2020

@author: vivek
"""

# gui
# tkinter - built in
# Flask or Django are good for building web apps
# ipywidgets is good for building dashboards
# PyGame is good for game development

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# interact functionality with gui

def f(x):
    return x
interact(f, x=10); # gives a slider that can be varied to change the output
interact(f, x=True); # with boolean the function creates a check box
interact(f, x='Hi there!'); # with strings the funciton creates a text box

# interact decorator - to do the same as above
@interact(x=True, y=1.0) # if we pass y=fixed(1.0) then the use will not be able to change the value of the variable
def g(x, y):
    return (x, y)

# Widget abbreviations
'''
Keyword argument - Widget
`True` or `False` - Checkbox
`'Hi there'` - Text
`value` or `(min,max)` or `(min,max,step)` if integers are passed - IntSlider
`value` or `(min,max)` or `(min,max,step)` if floats are passed - FloatSlider
`['orange','apple']` or `{'one':1,'two':2}` - Dropdown
'''
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=10)); # Can call the IntSlider to get more specific
interact(f, x=(0,4)); # Instead of calling IntSlider, we can use Tuples to pass Min,Max for slider
interact(f, x=(0,8,2)); # (min, max, step)

# this also works with funciton decorators
@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x
interact(f, x=['apples','oranges']); # this will show a drop down menu, apple will appear in the drop down and will also be the output when you select apple in the drop down
interact(f, x={'one': 10, 'two': 20}); # this will show a drop down, but one will appear in the drop down however 10 will be returned when you chose one from the drop down

# Using function annotations with interact
def f(x:True):  # Python 3 only
    return x
interact(f);


# interactive - useful when you want to reuse the widgets that have already been produced
# or when you want to access the data that is bound to the user interface controls
# unlike interact the return value of the function is not displayed automatically
# instead you can use display() to display the return value
from IPython.display import display
def f(a, b):
    display(a + b)
    return a+b
w = interactive(f, a=10, b=20)
type(w)
w.children # in this case it is, two integer sliders as well as the output
display(w) # displays the return value
w.kwargs
w.result


# gui widget basics
# Widgets are eventful python objects that have a representation in the browser, often as a control like a slider, textbox, etc.
import ipywidgets as widgets
# repr
# Widgets have their own display repr which allows them to be displayed using IPython's display framework. Constructing and returning an IntSlider automatically displays the widget (as seen below). Widgets are displayed inside the output area below the code cell. Clearing cell output will also remove the widget.
widgets.IntSlider()

# You can also explicitly display the widget using display(...).
from IPython.display import display
w = widgets.IntSlider()
display(w)

# Multiple display() calls
# If you display the same widget twice, the displayed instances in the front-end will remain in sync with each other. 
# Try dragging the slider below and watch the slider above.
display(w)

# Closing widgets
w.close()

# Widget properties

w = widgets.IntSlider()
display(w)
w.value
w.value=100 # Similarly, to set a widget's value, you can set its value property.
w.keys

widgets.Text(value='Hello World!', disabled=True) # Shorthand for setting the initial values of widget properties

# Linking two similar widgets
# If you need to display the same value two different ways, you'll have to use two different widgets. 
# Instead of attempting to manually synchronize the values of the two widgets, you can use the link or jslink function to link two properties together
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)
mylink = widgets.jslink((a, 'value'), (b, 'value'))
mylink.unlink() # Unlinking widgets






