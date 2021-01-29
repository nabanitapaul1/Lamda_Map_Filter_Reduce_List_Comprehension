# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:59:54 2021

@author: Nabanita Paul
"""

## List Comprehension

a_list =[1,2,3,4,8,100,50]

def square(a_list):
    sq_list =[]
    for i in a_list:
        sq_list.append(i*i)
        
    return sq_list
square(a_list)

sq_list = [i*i for i in a_list]
sq_list

# even numbers 

even_list = [i*i for i in a_list if i%2==0]
even_list
odd_list = [i*i for i in a_list if i%2!=0]
odd_list
