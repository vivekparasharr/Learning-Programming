# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:19:46 2020

@author: vivek
"""


import math
help(math)

# rounding functions
math.floor(4.35)
math.ceil(4.35)
round(4.35) # not part of math module
round(5.5) # python break 0.5 split by rounding to nearest even number

#mathematical constants
math.pi
math.e
math.inf
math.nan

#logarithmic function
math.log(math.e) # 1.0, since if we dont specify the base then the default base is e
math.log(100,10) # what number do i have to take 10 to the power of, to get 100

#a raised to power b
10**2 # 100

#trignometry
math.sin(10) # -0.5440211108893698
math.degrees(math.pi/2) # 90 degrees
math.radians(180) # 3.141592653589793


import random
help(random)
random.seed(101) # setting a seed is optional if you want to 
random.randint(0,100) # returns random number between 0-100

# sampling
# create a random list of number as the population
l=list(range(1,20))
# pick up one number
random.choice(l)
# pick up sample of ten numbers with replacement
random.choices(population=l, k=10) 
# without replacement
random.sample(population=l, k=10) 

# shuffle a list
random.shuffle(l) # in-place method, permanently shuffles elements of the list

# distributions
random.uniform(a=0,b=100) # randomly returns a number between 0-100. its called uniform distribution because the likelihood of picking any number is the same
random.gauss(mu=0, sigma=1) # normal/gaussian distribution centered (mean) at zero, with a standard deviation of 1




