
# generate a certain number of random variables
# numpy.random.randn(100) # generates a 100 random numbers
import numpy
counter=0
for i in numpy.random.randn(100):
# this loop can be used to iterate over these 100 random numbers
    if i >=-1 and i<=1:
        counter+=1
result=counter/100
print(result)

