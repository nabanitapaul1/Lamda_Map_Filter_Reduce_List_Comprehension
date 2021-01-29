# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:41:52 2021

@author: Nabanita Paul
"""

## Filter Function

def even(num):
    if num%2==0:
        return True

a_list =[1,2,6,8,14,56,98]
list(filter(even,a_list))
list(map(even,a_list))

 # or 
even = lambda a_num:a_num%2==0
list(filter(even,a_list))

list(map(even,a_list))

## Reduce Function

from functools import reduce

a_list = [1,2,3,4,7,10,15,16]

prod = reduce((lambda x,y:x*y),a_list)
prod

greatest= reduce((lambda x,y: y if(y>x) else x),a_list)
greatest

smallest  = reduce((lambda x,y: x if(x<y) else y),a_list)
smallest


