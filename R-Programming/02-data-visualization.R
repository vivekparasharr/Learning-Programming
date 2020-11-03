
# data visualization

library(tidyverse)

# Do cars with big engines use more fuel than cars with small engines? 

ggplot2::mpg
# displ - engine displacement, in litres
# hwy - highway miles per gallon

# syntax
# ggplot(data = <DATA>) + 
#   <GEOM_FUNCTION>(mapping = aes(<MAPPINGS>))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))
# geom_point() adds a layer of points to your plot, which creates a scatterplot
# mapping argument is always paired with aes(), and the x and y arguments of aes() specify which variables to map to the x and y axes

# number of rows and columns in a dataset
nrow(mpg)
ncol(mpg)

# get to know more about the dataset using help
?mpg

# Make a scatterplot of hwy vs cyl
ggplot(data=mpg) +
  geom_point(mapping=aes(x=hwy, y=cyl))
# hwy - highway miles per gallon
# cyl - number of cylinders

# Make a scatterplot of class vs drv
ggplot(data=mpg) +
  geom_point(mapping=aes(x=class, y=drv))
# class - "type" of car
# drv - the type of drive train, where f = front-wheel drive, r = rear wheel drive, 4 = 4wd

