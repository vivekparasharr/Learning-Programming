# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:42:56 2020

@author: vivek
"""

'''
Widget Styling
style vs. layout
There are two ways to change the appearance of widgets in the browser. The first is through the layout attribute which exposes layout-related CSS properties for the top-level DOM element of widgets, such as margins and positioning. The second is through the style attribute which exposes non-layout related attributes like button color and font weight. While layout is general to all widgets and containers of widgets, style offers tools specific to each type of widget.

Thorough understanding of all that layout has to offer requires knowledge of front-end web development, including HTML and CSS. This section provides a brief overview of things that can be adjusted using layout. However, the full set of tools are provided in the separate notebook Advanced Widget Styling with Layout.

To learn more about web development, including HTML and CSS, check out the course Python and Django Full Stack Web Developer Bootcamp

Basic styling is more intuitive as it relates directly to each type of widget. Here we provide a set of helpful examples of the style attribute.

The layout attribute
Jupyter interactive widgets have a layout attribute exposing a number of CSS properties that impact how widgets are laid out. These properties map to the values of the CSS properties of the same name (underscores being replaced with dashes), applied to the top DOM elements of the corresponding widget.

Sizes
height
width
max_height
max_width
min_height
min_width

Display
visibility
display
overflow
overflow_x
overflow_y

Box model
border
margin
padding

Positioning
top
left
bottom
right

Flexbox
order
flex_flow
align_items
flex
align_self
align_content
justify_content
A quick example of layout
'''

import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider()
display(w)

# change two of the properties of this widget: margin and height
w.layout.margin = 'auto'
w.layout.height = '75px'

# assign w's layout settings to x
x = widgets.IntSlider(value=15,description='New slider')
display(x)
x.layout = w.layout # assign w's layout settings to x


'''
Predefined styles
Before we investigate the style attribute, it should be noted that many widgets offer a list of pre-defined styles that can be passed as arguments during creation.

For example, the Button widget has a button_style attribute that may take 5 different values:

'primary'
'success'
'info'
'warning'
'danger'
besides the default empty string ''.
'''
import ipywidgets as widgets

widgets.Button(description='Ordinary Button', button_style='')

widgets.Button(description='Danger Button', button_style='danger')


'''
The style attribute
While the layout attribute only exposes layout-related CSS properties for the top-level DOM element of widgets, the style attribute is used to expose non-layout related styling attributes of widgets.

However, the properties of the style atribute are specific to each widget type.
'''

b1 = widgets.Button(description='Custom color')
b1.style.button_color = 'lightgreen'
b1
b1.style.keys # get a list of the style attributes for a widget with the keys property

b2 = widgets.Button()
b2.style = b1.style # Just like the layout attribute, widget styles can be assigned to other widgets.
b2

# Widget styling attributes are specific to each widget type.
s1 = widgets.IntSlider(description='Blue handle')
s1.style.handle_color = 'lightblue'
s1

# Widget style traits
'''
These are traits that belong to some of the more common widgets:

Button
button_color
font_weight

IntSlider, FloatSlider, IntRangeSlider, FloatRangeSlider
description_width
handle_color

IntProgress, FloatProgress
bar_color
description_width

Most others such as ToggleButton, Checkbox, Dropdown, RadioButtons, Select and Text only have description_width as an adjustable trait.
'''

########################################


'''
Advanced Widget Styling with Layout
This notebook expands on the Widget Styling lecture by describing the various HTML and CSS adjustments that can be made through the layout attribute.

The layout attribute
Jupyter interactive widgets have a layout attribute exposing a number of CSS properties that impact how widgets are laid out.

Exposed CSS properties
The following properties map to the values of the CSS properties of the same name (underscores being replaced with dashes), applied to the top DOM elements of the corresponding widget.

Sizes
height
width
max_height
max_width
min_height
min_width

Display
visibility
display
overflow
overflow_x
overflow_y

Box model
border
margin
padding

Positioning
top
left
bottom
right

Flexbox
order
flex_flow
align_items
flex
align_self
align_content
justify_content

Shorthand CSS properties
You may have noticed that certain CSS properties such as margin-[top/right/bottom/left] seem to be missing. The same holds for padding-[top/right/bottom/left] etc.

In fact, you can atomically specify [top/right/bottom/left] margins via the margin attribute alone by passing the string '100px 150px 100px 80px' for a respectively top, right, bottom and left margins of 100, 150, 100 and 80 pixels.

Similarly, the flex attribute can hold values for flex-grow, flex-shrink and flex-basis. The border attribute is a shorthand property for border-width, border-style (required), and border-color.
'''

import ipywidgets as widgets
from IPython.display import display

