#! /usr/bin/python

import math
from math import sqrt
import cmath
import sys

print ('')
print ('**This program helps user to find out Quadratic Formula solutions**' )
print ('')

a= float(input("Please Enter A= "))
b= float(input("Please Enter B= "))
c= float(input("Please Enter C= "))

while a == 0 :
	print ('')
	print ('_______________')
	print ('A value can not be equal to 0')
	print ('Please ReEnter Values')	
	print('')
	
	a= float(input("Please Enter A= "))
	b= float(input("Please Enter B= "))
	c= float(input("Please Enter C= "))


top = b**2 - 4*a*c
bottom = sqrt(top)
First = (-b + bottom) / (2*a)
Second = (-b - bottom) / (2*a)

print('')
print('_______________')
print('')



print float(a),'x^2 +' ,float(b),'x +' ,float(c), '= 0'


print"x1: " + str(First)
print"x2: " + str(Second)

exit (0)
