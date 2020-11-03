#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:19:08 2017

@author: vivekparashar
"""

Input 2 numbers A and B from the user. Then perform basic numeric operations (+,-,*,/,**,%) on them
Output should look like:
A: 8
B: 3
Sum: 11.0
Difference: 5.0
Product: 24.0
Division: 2.6666666666666665
Power: 512.0
Modulo: 2.0
                                                                             
a = float(input("A: "))
b = float(input("B: "))
print('Sum:',a+b)
print('Difference:',a-b)
print('Product:',a*b)
print('Division:',a/b)
print('Power:',a**b)
print('Modulo:',a%b)



Write a Python program to convert degree to radian 
(hint 1: pi radians is equal to 180 degrees)
(hint 2: degree=pi/180 radians)

pi=22/7
degree = float(input("Input degree: "))
radian = degree*(pi/180)
print(radian)



Write a program to get the length and width of a rectange from the user and then display its area
(hint: area of a rectangle=length*width)

length = float(input("Input length: "))
width = float(input("Input width: "))
area = length*width
print(area)




Write a program to input radius of a circle from the user and then calculate its area and circumference
(hint: area=pi*(r**2) and circumference=2*pi*r)

import math
radius = float(input("Input radius: "))
area = math.pi*(radius**2)
circumference = 2*math.pi*radius
print(area)
print(circumference)




Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number
                                           
def prime(num):
    p=0
    for i in range(2,int(num)-1,1):
        if num%i==0:
            p=p+1
    return p

for i in range(2,10,1):
    if prime(i)==0:
        print(i)



Input a number from the user and print if it is even or odd
(hint: even numbers are divisible by 2)

num = float(input("Enter a number: "))
if num%2==0:
    print('Number is Even')
else:
    print('Number os Odd')



Input a number from user and then print all even numbers starting from 2 to that number
(hint: if user enters 8, then the program should print 2, 4, 6, 8)

num = float(input("Enter a number: "))
for i in range(2,int(num)+1,1):
    if i%2==0:
        print(i)
    else:
        continue


Write a program to input length of the two small sides and calculate the length of the longest side of a right angled triangle
a^2 + b^2 = c^2, where a and b are the legs and c is the hypotenuse (the longest side)

a = float(input("A: "))
b = float(input("B: "))
c = math.sqrt( (a**2) + (b**2) )
print ('C: ',c)





Write a program to generate and print 10 random numbers between 1 and 100
(hint: random.randint(1, 100) would give you 1 random number between 1 and 100)

import random
for i in range(1,10):
    print(random.randint(1,100))



Write a program to identify if a number is prime or not
(hint1: a prime number is only divisible by 1 and itself)
(hint2: Here are the first few prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, etc.)
(largest prime number under 1 million: 999983)

num = float(input("Enter a number (greater than 1): "))
p=0
for i in range(2,int(num)-1,1):
    if num%i==0:
        p=p+1
if p>0:
    print('Not Prime')
else:
    print('Prime')
    



        



