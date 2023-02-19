# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 06:08:01 2022

@author: Ali

A prime number is a number that is only evenly divisible by itself and 1. 
For example, the number 5 is prime because it can only be evenly divided by 1 and 5.
 The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and
returns True if the argument is a prime number, or False otherwise. Use the function in a
program that prompts the user to enter a number and then displays a message indicating
whether the number is prime.
"""

def main():
    num = call_func()
    
    Boolean = is_prime(num)
    if Boolean == True:
        print('The entered number is prime.')
    else:
        print('The entered number is not prime.')
    
    
def call_func():
    number = int(input('Enter a number: '))
    return number

def is_prime(num):
    # Define a counter and initialize it to zero
    c = 0
    for n in range(1, num+1):
        if num % n == 0:
            b = 1
        else:
            b = 0
        c += b
    if c <= 2:
        # Index for boolean operator
        i = True
    else:
        i = False
    
    return i
        
            
main()