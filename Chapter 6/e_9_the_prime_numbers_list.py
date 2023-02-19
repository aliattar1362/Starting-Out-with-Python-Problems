# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 07:20:14 2022

@author: Ali

This exercise assumes you have already written the is_prime function in Programming
Exercise 8. Write another program that displays all of the prime numbers
 from 1 through 100.
The program should have a loop that calls the is_prime function.
"""

def main():
    for n in range(1, 101):
        Boolean = is_prime(n)
        if Boolean == True:
            print('The entered number', n, ' is prime.')
        else:
            print('The entered number', n, ' is not prime.')
            
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