#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:32:28 2024

@author: dohdohasskicker513
"""

# the bone of defining a function 
def my_func(num):
    num = (num * 2 +40)/10
    return num
value = my_func(10)
print (value)
# but why do we need to assign a new name to num in the local calculation
# new_num = (num * 2 + 40)/10

# the textbook sample
def my_func(num):
    new_num = (num * 2 + 40)/10
    return new_num
value = my_func(10)
print (value)

#it prints information about the function object itself. 
#Specifically, <function my_func at 0x15b9e62a0> 
#indicates that my_func is a function object 
#located at memory address 0x15b9e62a0.
print (my_func())
# if you want to see the code, inspect 
# import first

#
my_global = 10
def my_func(): #remember the parentesises
    my_local = 20 
    return my_global * my_local

print (my_func()) # would return the result as no requirement for positional
#argument

print (my_global) # 10
print (my_local) #not defined 


names_2021 = [' jeff', 'molly', 'YIJIA', 'Jon', 'RaHuL', 'noah ', 'Bob']
def name_fixer (n):
    new_n= [n.strip().capitalize() for n in names_2021]
    return new_n
fixed_names_2021 = name_fixer (names_2021)
print(fixed_names_2021)



#try this instead
def name_fixer(n):
    n = n.strip().capitalize()
    if n == 'Jon':
        result = 'John'
    elif n == 'Bob':
        result = 'Bob does not work here any more!'
    elif n == 'Simo n':
        result = 'Simon'
    else:
        result = n
    return result
fixed_names = [name_fixer(n) for n in names_2021]
print(fixed_names)
