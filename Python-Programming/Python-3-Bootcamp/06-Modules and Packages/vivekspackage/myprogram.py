# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:50:42 2020

@author: vivek
"""

# example - import from a module
from mymodule import my_func
my_func()

# example - import from a package

from MyMainPackage import mainscript
from MyMainPackage.SubPackage import mysubscript

mainscript.report_main()
mysubscript.sub_report()

