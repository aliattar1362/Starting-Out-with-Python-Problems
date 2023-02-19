# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 23:02:01 2022

@author: Ali
In this chapter you saw an example of how to write an algorithm that determines whether
a number is even or odd. Write a program that generates 100 random numbers, and keeps
a count of how many of those random numbers are even and how many are odd.
"""
import random
TOTAL_NUM = 100


def main():
    val_even = 0
    val_odd = 0
    t_even = 0
    t_odd = 0
    
    for n in range(TOTAL_NUM):
        number = random.randrange(999)
        print(number)
        val_even, val_odd = deter_func(number)
        t_even += val_even 
        t_odd += val_odd  
        
    print('Among these numbers', t_odd, 'are odd numbers and ', t_even, 'are even numbers.')
        
def deter_func(num):
    remain = num%2
    if remain == 0:
        value_even = 1
        value_odd = 0
    else:
        value_even = 0
        value_odd = 1
        
    return (value_even, value_odd)
        
main()