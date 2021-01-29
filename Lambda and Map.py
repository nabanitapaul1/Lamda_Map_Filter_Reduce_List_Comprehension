# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:06:58 2021

@author: Nabanita Paul
"""

### Lambda Function

## addition
def addition(a,b):
    return a+b
addition(1,2)
addition = lambda  a,b:a+b
addition(8,9)

## Even Number

def even(a_num):
    if a_num%2 == 0:
        return True
   
even(28)

even = lambda num:num%2==0
even(28)

## Sum of three numbers

def addition(x,y,z):
    sum_three= x+y+z
    return sum_three
addition(2,4,5)

addition =  lambda x,y,z:x+y+z
addition(2, 7,9)


## Map Function

def even_or_odd(a_num):
    if a_num%2==0:
        print("The {} is even number".format(a_num))
    else:
        print("The {} is odd number".format(a_num))
even_or_odd(24)  
a_list = [1,2,3,4,8,9]
for a_num in a_list:
    print(even_or_odd(a_num))


# Using map function
a_list1 = map(even_or_odd,a_list)
a_list1 = list(a_list1)
